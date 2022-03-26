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
    priceByBox = models.DecimalField(max_digits=100000, decimal_places=2)
    stockByBox = models.IntegerField()
    peicePerBox = models.IntegerField()



class order(models.Model):
    by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, related_name='Customer')
    prodJson = models.TextField()
    orderDateTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
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
    Total = models.DecimalField(max_digits=10000000, decimal_places=2, null=True, blank=True)






class favourite(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
	added = models.IntegerField()