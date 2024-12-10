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
    class Meta :
        model = Sale 
        fields = "__all__"