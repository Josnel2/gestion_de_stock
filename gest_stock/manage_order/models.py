from django.db import models
from django.contrib.auth.models import User
from manage_order.enums import StatusEnum, StatusOrderEnum

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du produit")
    description = models.TextField(null=True, blank=True, verbose_name="Description du produit")
    reference = models.CharField(max_length=100, unique=True, verbose_name="Référence")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
    category = models.CharField(max_length=255, verbose_name="Catégorie")
    status = models.CharField(choices=StatusEnum.choices, max_length=50, verbose_name="Statut")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Quantité en stock")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    def __str__(self):
        return f"{self.reference} - {self.name}"

    def is_in_stock(self):
        return self.stock_quantity > 0


class Provider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du fournisseur")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Adresse e-mail")
    phone_number = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    address = models.TextField(verbose_name="Adresse")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="providers", verbose_name="Produit fourni")

    def __str__(self):
        return self.name


class Order(models.Model):

    status = models.CharField( max_length=20, choices=StatusOrderEnum.choices, default=StatusOrderEnum.pending, verbose_name="Statut")
    order_date = models.DateField(auto_now_add=True, verbose_name="Date de la commande")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name="Fournisseur")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produit")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Prix total")
    delivery_address = models.TextField(verbose_name="Adresse de livraison", blank=True, null=True)
    is_paid = models.BooleanField(default=False, verbose_name="Commande payée")

    def save(self, *args, **kwargs):
        if self.product.stock_quantity < self.quantity:
            raise ValueError(
                f"Stock insuffisant pour '{self.product.name}'. Quantité disponible : {self.product.stock_quantity}"
            )
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Commande #{self.pk} - {self.product.name} ({self.quantity})"


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produit vendu")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    quantity = models.PositiveIntegerField(verbose_name="Quantité vendue")
    sale_date = models.DateField(auto_now_add=True, verbose_name="Date de la vente")

    def __str__(self):
        return f"Vente #{self.pk} - {self.product.name} ({self.quantity})"

    @property
    def total_amount(self):
        return self.product.price * self.quantity
    

