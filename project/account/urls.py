from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import UsersView, RegisterView, LoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

userRouter = DefaultRouter()
userRouter.register('userslist', UsersView)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="reg"),
    path("login/", LoginView.as_view(), name="log"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += userRouter.urls
