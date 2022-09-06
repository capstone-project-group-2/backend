from django.db import models
from account.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', blank=True , null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product/', blank=True , null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    review = models.DecimalField(decimal_places=1,max_digits=2)