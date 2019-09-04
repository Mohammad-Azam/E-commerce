from django import template
from product.models import Order

register = template.Library()


@register.filter(name='ordercount')
def ordercount(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():

            #print(items.count())
            return qs[0].items.count()
    return 0
