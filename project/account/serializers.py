from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            newUser = User (
                email=validated_data['email'],
                username=validated_data['username']
            )
            newUser.set_password(validated_data['password'])
            newUser.save()
            return newUser