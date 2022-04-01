from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    # Main Shop Home Page For Customer
    path('', index, name='index'),


    path('cart/', cart, name="cart"),
    path('cart/pending/', pending, name="pending"),
    path('cart/processing/', processing, name="processing"),
    path('cart/completed/', completed, name="completed"),
    path('cart/cancelled/', cancelled, name="cancelled"),


    path('favourites/', favourites, name="favourites"),
    path('addtofav/', addtofav, name="addtofav"),
    path('add-to-cart/', addcart, name="add-to-cart"),
    path('delete/<int:id>/', delete, name="delete"),
    path('total/', total, name="total"),
    path('checkout/', checkout, name="checkout"),
    path('confirm/checkout/', confirmcheckout, name="confirmcheckout"),


    path('products/', productspage, name="products"),
    path('brand/<str:brand>/', brandspage, name="brand"),
    path('category/<str:category>/', categoryspage, name="category"),
    path('color/<str:color>/', colorspage, name="color"),

    # Main Home Page For Staff
]