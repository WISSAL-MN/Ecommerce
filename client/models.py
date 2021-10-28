from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Client (models.Model):
    name=models.CharField(max_length=200,null=True ,blank=True)
    fammily_name=models.CharField(max_length=200,null=True, blank=True)
    phone=models.IntegerField()