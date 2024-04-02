
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class User(AbstractUser):
    role = models.CharField(max_length=100, blank=True, null=True)
    is_dealer = models.BooleanField(default=False)
    # Add related_name to avoid clash
    groups = models.ManyToManyField(Group, related_name='productapp_users')
    user_permissions = models.ManyToManyField(Permission, related_name='productapp_users')


class Product(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    image = models.CharField(max_length=2083, default='default_image_url.jpg')
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    

    def __str__(self):
        return self.name

