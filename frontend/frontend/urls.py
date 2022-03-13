"""frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('productref/<slug>/', views.productref),
    path('cart/', views.Cart, name='cart'),
    path('add-to-cart/<slug>/', views.addCart, name='addCart'),
    path('checkout/', views.CHeckout, name='checkout'),
    path('quanInc/<slug>/', views.quanInc, name='quanInc'),
    path('quanDec/<slug>/', views.quanDec, name='quanDec'),
    path('prodDelete/<slug>/', views.prodDelete, name='prodDelete'),
    path('recovery/', views.recovery, name='recovery'),
    path('logout/', views.LogOut, name='logout'),
]

