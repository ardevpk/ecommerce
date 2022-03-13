from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=5000)
    comp = models.BooleanField(default=False)