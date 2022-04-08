from unicodedata import name
from django.urls import path
from .views import *
from .pdf import pdf
from .staff import *

urlpatterns = [
    # Main Shop Home Page For Customer
    path('', index, name='index'),


    path('cart/', cart, name="cart"),
    path('cart/pending/', pending, name="pending"),
    path('cart/pending/change/<int:id>/', changepage, name="changepage"),
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
    

    path("cart/pending/pdf/<int:id>/" , pdf, name="pdf"),


    # Staff Views Start From Here
    path('staff/pending/', staffpending, name="staffpending"),
    path('staff/processing/', staffprocessing, name="staffprocessing"),
    path('staff/completed/', staffcompleted, name="staffcompleted"),
    path('staff/cancelled/', staffcancelled, name="staffcancelled"),



    path('staff/pdf/<int:id>/', pdf, name="staffpdf"),


    path('staff/recovery/', recovery, name="recovery"),
    path('staff/return/', returns, name="returns"),



    path('staff/order/status/change/<int:id>/<str:name>/', changesaffstats, name="changesaffstats"),
]