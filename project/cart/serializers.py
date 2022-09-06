from rest_framework import serializers
from cart.models import *

class CartSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(decimal_places=2, max_digits=6,source='product.price')
    product_image = serializers.ImageField(source='product.image')
    class Meta:
        model = Cart
        fields = '__all__'

class CartQTYSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'