from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	is_verified = models.BooleanField(default=False)
	phrase = models.CharField(max_length=254, null=True, blank=True)
	def __str__(self):
		return self.username