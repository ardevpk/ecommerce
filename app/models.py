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
    def __str__(self):
        return self.name



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
    carttotal = models.DecimalField(max_digits=100000000, decimal_places=3, null=True, blank=True)
    percent = models.DecimalField(max_digits=100000000, decimal_places=3, null=True, blank=True)
    saved = models.DecimalField(max_digits=100000000, decimal_places=3, null=True, blank=True)
    total = models.DecimalField(max_digits=100000000, decimal_places=3, null=True, blank=True)
    def __str__(self):
        return self.user.username






class favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    added = models.IntegerField()
    def __str__(self):
        return self.user.username







class city(models.Model):
    city = models.CharField(max_length=254)
    def __str__(self):
        return self.city


CITY_ID = 2
class userdetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    OnCashPercentage = models.DecimalField(max_digits=100000000, decimal_places=3, default=0, null=True, blank=True)
    OnCreditPercentage = models.DecimalField(max_digits=100000000, decimal_places=3, default=0, null=True, blank=True)
    location = models.CharField(max_length=254)
    city = models.ForeignKey(city, default=CITY_ID, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=254, default='pakistan', null=True, blank=True)
    total = models.DecimalField(max_digits=100000000, decimal_places=3, default=0.000, null=True, blank=True)
    def __str__(self):
        return self.user.username






class RECOVERY(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, related_name='CustomerRecovery')
    cash = models.DecimalField(max_digits=100000000, decimal_places=3, default=0.000)
    orderid = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=f'images/recovery/', null=True, blank=True)
    recoveryBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, related_name='StaffRecovery')
    date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.user.username





class RETURNS(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, related_name='CustomerReturns')
    cash = models.DecimalField(max_digits=100000000, decimal_places=3, default=0.000)
    orderid = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=f'images/recovery/', null=True, blank=True)
    returnTakenBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, related_name='StaffReturns')
    date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.user.username