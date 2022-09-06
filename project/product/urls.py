from django.urls import path
from product.views import *

urlpatterns = [
    path('category/',CategoryAPI.as_view()),
    path('<int:product_id>/reviews/',GetReviewsByProductId.as_view()),
    path('newreview/',CreateReview.as_view()),
    path('<int:num>/',Product_FilterAPI.as_view()),
    path('product/id/<int:id>/',GetProductById.as_view()),
    path('product/',ProductAPI.as_view()),

]