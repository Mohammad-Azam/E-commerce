from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    overview = models.TextField()
    pack=models.CharField(max_length=15)
    usage = models.CharField(max_length=50)
    color = models.CharField(max_length=20 )
    minimum_set = models.CharField(max_length=20)
    material = models.CharField(max_length=25)
    image = models.ImageField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug': self.slug })
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={ 'slug': self.slug })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={ 'slug': self.slug })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()

        return total

