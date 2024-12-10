from django.contrib import admin
from.models import Product,Provider,Order,Sale
# Register your models here.

admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Order)
admin.site.register(Sale)