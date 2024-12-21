from rest_framework import serializers
from manage_order.models import Product,Provider,Order,Sale


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
        
class ProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields = "__all__"
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"
        

class SaleSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()  

    class Meta:
        model = Sale
        fields = ['id', 'product', 'user', 'quantity', 'sale_date', 'total_amount']
        read_only_fields = ['sale_date']  

