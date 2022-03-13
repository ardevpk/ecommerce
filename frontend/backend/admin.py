from django.contrib import admin
from backend.models import product, cart, checkout, client, employee, cOrders
# Register your models here.

class productPage(admin.ModelAdmin):
    list_display = ('brand', 'name', 'price', 'tag')

class cartPage(admin.ModelAdmin):
    list_display = ('cartName', 'prodBrand', 'prodName')

class checkoutPage(admin.ModelAdmin):
    list_display = ('checkoutName', 'toPay', 'date')

class clientPage(admin.ModelAdmin):
    list_display = ('clShopName', 'clPhone', 'clPendingBalance', 'clPaidBalance', 'clOnCredit')


class employeePage(admin.ModelAdmin):
    list_display = ('ename', 'eCompOrders', 'eTakenProdPrice', 'eRecievenCash')


class cOrdersPage(admin.ModelAdmin):
    list_display = ('orderByName', 'orderByPhone', 'cBy', 'cOrderPrice', 'cOnDate')


admin.site.register(product, productPage)
admin.site.register(cart, cartPage)
admin.site.register(checkout, checkoutPage)
admin.site.register(client, clientPage)
admin.site.register(employee, employeePage)
admin.site.register(cOrders, cOrdersPage)