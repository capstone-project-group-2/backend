from django.urls import path
from product.views import *

urlpatterns = [
    path('category/',CategoryAPI.as_view()),
    path('product/',ProductAPI.as_view()),

]
