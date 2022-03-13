from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=288)
    tag = models.CharField(max_length=12)
    date = models.DateField()
    image = models.ImageField(upload_to='uploads/')

class client(models.Model):
    name = models.CharField(max_length=24)
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=24)
    phone = models.CharField(max_length=24)
    shopName = models.CharField(max_length=24)
    address = models.CharField(max_length=24)
    userCreatedDate = models.DateField(max_length=24)
    UserOrders = models.CharField(max_length=24)
    userPaid = models.CharField(max_length=24)
    userRemainine = models.CharField(max_length=24)
