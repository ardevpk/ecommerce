from django.urls import path
from .views import *

urlpatterns = [
    # Main Shop Home Page For Customer
    path('', index),
    path('cart/', cart),
    path('addtofav/', addtofav),
    path('add-to-cart/', addcart),
    path('delete/<int:id>/', delete),

    # Main Home Page For Staff
]