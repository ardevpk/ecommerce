from django.urls import path
from .views import *

urlpatterns = [
    # Main Shop Home Page For Customer
    path('', index),
    path('cart/', cart, name='cart'),
    path('add-to-cart/', addcart, name='addcart'),
    path('delete/<int:id>/', delete, name='delete'),
    path('addtofav/', addtofav, name='addtofav'),

    # Main Home Page For Staff
]