from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    # Main Shop Home Page For Customer
    path('', index, name='index'),
    path('cart/', cart, name="cart"),
    path('addtofav/', addtofav, name="addtofav"),
    path('add-to-cart/', addcart, name="add-to-cart"),
    path('delete/<int:id>/', delete, name="delete"),


    path('products/', productspage, name="products"),

    # Main Home Page For Staff
]