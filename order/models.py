from django.db import models

# Create your models here.
class Order(models.Model):
    total_price=models.FloatField(null=True)
    id=models.IntegerField(uudi=4)
    
