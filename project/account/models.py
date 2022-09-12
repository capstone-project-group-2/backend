from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = PhoneNumberField(null=False, blank=False, unique=True)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    mobile = PhoneNumberField(null=False, blank=False, unique=True)
    address1 = AddressField()
    address2 = AddressField(related_name='+', blank=True, null=True)    
