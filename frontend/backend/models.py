from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=500)
    tag = models.CharField(max_length=500)
    desc = models.CharField(max_length=10000)
    color = models.CharField(max_length=500)
    price = models.IntegerField()
    brand = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/', default='https://via.placeholder.com/500x750')
    slug = AutoSlugField(populate_from='name')
    

class cart(models.Model):
    cartName = models.ForeignKey(User, on_delete=models.CASCADE)
    prodId = models.IntegerField()
    prodPrice = models.IntegerField()
    prodTag = models.CharField(max_length=5000)
    prodName = models.CharField(max_length=5000)
    prodBrand = models.CharField(max_length=5000)
    prodImage = models.CharField(max_length=5000, default='https://via.placeholder.com/100x100')
    prodQuan = models.IntegerField()
    perProdTotal = models.IntegerField()
    def __str__(self):
        return str(self.cartName)


class client(models.Model):
    clName = models.ForeignKey(User, on_delete=models.CASCADE)
    clShopName = models.CharField(max_length=500)
    clShopAddress = models.CharField(max_length=500)
    clPhone = models.IntegerField()
    clPendingBalance = models.IntegerField()
    clPaidBalance = models.IntegerField()
    clOnCredit = models.BooleanField(default=False)
    def __str__(self):
        return self.clName


class checkout(models.Model):
    checkoutName = models.ForeignKey(User, on_delete=models.CASCADE)
    yourName = models.CharField(max_length=500)
    shopName = models.CharField(max_length=500)
    phone = models.IntegerField()
    address = models.CharField(max_length=500)
    aod = models.CharField(max_length=10000, default="")
    toPay = models.IntegerField()
    checkoutProdId = models.CharField(max_length=1000)
    checkoutProdName = models.CharField(max_length=10000)
    checkoutProdQuan = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.checkoutName)




class employee(models.Model):
    ename = models.ForeignKey(User, on_delete=models.CASCADE)
    eCompOrders =  models.IntegerField()
    eTakenProdPrice =  models.IntegerField()
    eRecievenCash =  models.IntegerField()
    def __str__(self):
        return self.ename

class eRecievenCash(models.Model):
    eRname = models.ForeignKey(employee, on_delete=models.CASCADE)
    eRDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ename


class cOrders(models.Model):
    orderByName = models.ForeignKey(User, on_delete=models.CASCADE)
    orderByPhone = models.IntegerField()
    orderByAddress = models.CharField(max_length=500)
    cBy = models.ForeignKey(employee, on_delete=models.CASCADE)
    cOnDate = models.DateField(auto_now_add=True)
    cOrderPrice = models.IntegerField()
    cOrderProdName = models.CharField(max_length=500)
    cOrderProdQuan = models.CharField(max_length=500)
    cOrderProdId = models.CharField(max_length=500)
    def __str__(self):
        return self.orderByName
    def __str__(self):
        return self.cBy


class returns(models.Model):
    rByName = models.CharField(max_length=500)
    rByPhone = models.IntegerField()
    rByAddress = models.CharField(max_length=500)
    rTakenBy = models.ForeignKey(employee, on_delete=models.CASCADE)
    rOrderPrice = models.IntegerField()
    rOrderProdDetail = models.CharField(max_length=10000)
    rOnDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.rTakenBy


class recovery(models.Model):
    recByName = models.ForeignKey(employee, on_delete=models.CASCADE)
    recByWhichShop= models.ForeignKey(User, on_delete=models.CASCADE)
    recPrice = models.IntegerField()
    rOnDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.recByName
    def __str__(self):
        return self.recByWhichShop