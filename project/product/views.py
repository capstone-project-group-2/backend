from rest_framework.generics import ListAPIView
from product.serializers import *
from product.models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductAPI(APIView):
    def get(self , request):
        product_list = list(Product.objects.values('id', 'name', 'category__name', 'description', 'price', 'stock', 'image'))
        for product in product_list:
            product['image'] = 'https://localhost:8000.com/media/' + product['image']
        return Response(product_list)
