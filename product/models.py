from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True,unique=True
                        )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
class Product(models.Model):
    name      = models.CharField(max_length=200,blank=True,null=True)
    buyingPrice   = models.FloatField(blank=True,null=True)
    sellingPrice = models.FloatField(blank=True,null=True)
    quantity    = models.IntegerField(blank=True,null=True)
    description  = models.TextField(blank=True,null=True)
    image       = models.ImageField(blank=True,null=True)
    category  = models.ForeignKey('product.Category', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} - {self.buyingPrice}'
    class Meta:
        unique_together = ['name', 'description']
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'