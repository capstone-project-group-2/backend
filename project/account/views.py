from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User, Group

class ListUserView(APIView):
    def get(self, request):
        user_list = list(User.objects.filter(groups__name='Shopping users').values())

        return Response(user_list)

class SignupView(APIView):
    def post(self , request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user = User.objects.create_user(username, email, password)
        user.save()

        group = Group.objects.get(name='Shopping users')
        group.user_set.add(user)

        return Response(
            {
                "status":"success" ,
                'user_id' :user.id , 
            })

class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
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

class ReportLoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        try:
            user = User.objects.get(username=username)
            if user.groups.filter(name='Report Generator users'):
                if user.check_password(password):
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
            else:
                return Response({"error": "User does not have permission" }) 

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
