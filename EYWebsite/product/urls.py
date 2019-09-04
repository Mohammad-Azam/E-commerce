from django.contrib import admin
from django.conf.urls import url
from.import views

urlpatterns=[

    url(r'detail$',views.ItemDetailView.as_view(),name='detail'),
    url(r'order-summary', views.OrderSummaryView.as_view(), name='order-summary'),
    url(r'checkout', views.CheckoutView.as_view(), name='checkout'),
    url(r'add-to-cart', views.add_to_cart, name='add-to-cart'),
    url(r'remove-from-cart',views. remove_from_cart, name='remove-from-cart'),
    url('^search', views.search, name='search'),
]