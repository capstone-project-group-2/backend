from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField

class User(AbstractUser):
    is_superuser = models.BooleanField('admin status', default=False)
    is_staff = models.BooleanField('report generator status', default=False)
    is_customer = models.BooleanField('shopping user status', default=False)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Mobile Phone number')
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Full name')
    mobile = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Mobile number')
    address1 = AddressField()
    address2 = AddressField(related_name='+', blank=True, null=True)    
