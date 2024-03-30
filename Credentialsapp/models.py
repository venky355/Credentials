from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        USERS = 'USERS', 'Users'
        DEALER = 'DEALER', 'Dealer'

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.USERS)
    dealer_field = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
