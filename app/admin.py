from django.contrib import admin

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'category', 'stockByPeice', 'color', 'priceByBox')
    list_filter = ['brand', 'name', 'category', 'stockByPeice', 'color', 'priceByBox']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('by', 'orderDateTime', 'payment', 'status', 'CheckedBy')
    list_filter = ['by', 'orderDateTime', 'payment', 'status', 'CheckedBy']
    
class favouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'added')


class userdetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'percentage', 'location', 'city', 'country')
    list_filter = ['user', 'percentage', 'location', 'city', 'country']


admin.site.register(product, ProductAdmin)
admin.site.register(order, OrderAdmin)
admin.site.register(favourite, favouriteAdmin)
admin.site.register(city)
admin.site.register(userdetail, userdetailAdmin)