from rest_framework import serializers
from manage_order.models import Product,Provider


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
        
class ProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields = "__all__"