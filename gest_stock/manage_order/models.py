from django.db import models
from django.contrib.auth.models import User
from manage_order.enums import StatusEnum, StatusOrderEnum

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du produit")
    description = models.TextField(null=True, blank=True)
    reference = models.CharField(max_length=100, unique=True, verbose_name="Référence")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255)
    status = models.CharField(choices=StatusEnum.choices, max_length=255)
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Quantité en stock")
    

    def __str__(self):
        return f"{self.pk} - {self.name}"

class Provider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du fournisseur")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Adresse e-mail")
    phone_number = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    address = models.TextField(verbose_name="Adresse")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="providers_in_manage_order", default=None)

    def __str__(self):
        return self.name


class Order(models.Model):
    status = models.CharField(max_length=20, choices=StatusOrderEnum, default='pending', verbose_name="Statut de la commande")
    order_date = models.DateField(auto_now_add=True, verbose_name="Date de la commande")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name="Fournisseur")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produit")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix total")
    delivery_address = models.TextField(verbose_name="Adresse de livraison", blank=True, null=True)
    is_paid = models.BooleanField(default=False, verbose_name="Commande payée")

    def save(self, *args, **kwargs):
        if self.product and self.quantity:
            self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Commande #{self.pk} - {self.product.name} par {self.user.username}"
