from rest_framework import serializers
from product.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1
    def create(self, validated_data):
        print (validated_data)
        return Review.objects.create(**validated_data)