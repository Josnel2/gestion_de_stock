from django.db import models
from manage_order.enums import StatusEnum

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du produit")
    description = models.TextField(null=True, blank=True)
    reference = models.CharField(max_length=100, unique=True, verbose_name="Référence")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255)
    status = models.CharField(choices = StatusEnum.choices , max_length=255 )
    stock_quantity = models.PositiveIntegerField(default=0 , verbose_name="Quantité en stock")  
    min_threshold = models.PositiveIntegerField(default=1) 

    def __str__(self):
     return f"{self.pk} - {self.name}"

