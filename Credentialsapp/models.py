

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    dealer_details = models.CharField(max_length=100, blank=True, null=True)
    

    class Role(models.TextChoices):
        USERS = 'users', 'Users'
        DEALER = 'dealer', 'Dealer'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USERS)    

    def __str__(self):
        return self.username

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    image = models.CharField(max_length=2083, default='default_image_url.jpg')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s wishlist: {self.product.name}"
