from django.urls import path
from wishlist.views import WishlistAPI

urlpatterns = [
    path('', WishlistAPI.as_view()),
]