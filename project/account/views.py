from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import generics

from .serializers import UserSerializer, RegisterSerializer
from .models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
            if user:
                if user.password == password:

                    refresh = RefreshToken.for_user(user)

                    return Response(
                        {
                            "status":"success" ,
                            'user_id' :user.id , 
                            'refresh': str(refresh),
                            'access': str(refresh.access_token)
                        })
                else:
                    return Response({"error": "Wrong Password" }) 

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')