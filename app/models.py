from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
# Create your models here.


class product(models.Model):
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    details = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=254)
    image = models.ImageField(upload_to=f'images/')
    priceByBox = models.IntegerField()
    stockByPeice = models.IntegerField()
    peicePerBox = models.IntegerField()
    discount = models.BooleanField(default=True)



class order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, related_name='Customer')
    prodJson = models.TextField()
    orderDateTime = models.DateTimeField(null=True, blank=True)
    PAYMENT_CHOICES = [
        ('CREDIT', 'Credit'),
        ('CASH', 'Cash')
    ]
    payment = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default="CASH", null=True, blank=True)
    APPROVED_CHOICES = [
        ('INCART', 'InCart'),
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(max_length=100, choices=APPROVED_CHOICES, default="INCART", null=True, blank=True)
    CheckedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, related_name='Staff', null=True, blank=True)
    CheckedDate = models.DateTimeField(null=True, blank=True)
    carttotal = models.IntegerField(null=True, blank=True)
    percent = models.IntegerField(null=True, blank=True)
    saved = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)






class favourite(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
	added = models.IntegerField()







class city(models.Model):
    city = models.CharField(max_length=254)
    def __str__(self):
        return self.city


CITY_ID = 2
class userdetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    percentage = models.IntegerField(default=70, null=True, blank=True)
    location = models.CharField(max_length=254)
    city = models.ForeignKey(city, default=CITY_ID, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=254, default='pakistan', null=True, blank=True)