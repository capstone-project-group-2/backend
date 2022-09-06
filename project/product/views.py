from rest_framework.generics import ListAPIView, CreateAPIView
from product.serializers import *
from product.models import *

class CategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class Product_FilterAPI(ListAPIView):
    serializer_class = ProductIDSerializer
    def get_queryset(self):
        num = self.kwargs['num']
        if num == 1:
            return Product.objects.filter(category_id__in=[2,3,4,5])
        elif num == 6:
            return Product.objects.filter(category_id__in=[7,8,9,10])
        elif num == 11:
            return Product.objects.filter(category_id__in=[12,13,14,15])
        elif num == 16:
            return Product.objects.filter(category_id__in=[17,18,19,20])
        else:
            return Product.objects.filter(category_id=num)
    
class GetProductById(ListAPIView):
    serializer_class = ProductListSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(id = id)

class GetReviewsByProductId(ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects.filter(product_id=product_id)

class CreateReview(CreateAPIView):
    serializer_class = ReviewSerializer
    