from django.urls import path
from cart.views import *

urlpatterns = [
    path("<int:id>/cart/", CartView.as_view(), name="cart"), 
    path("cart/<int:pk>", CartUpdateView.as_view({'put': 'update'}), name="updateCart"),
]
