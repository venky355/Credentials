from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        USERS = 'USERS', 'Users'
        DEALER = 'DEALER', 'Dealer'

    # role = models.CharField(max_length=50, choices=Role.choices, default=Role.USERS)
    role = models.CharField(max_length=100, blank=True, null=True)    
    is_dealer = models.BooleanField(default=False)
    # Add related_name to avoid clash
    groups = models.ManyToManyField(Group, related_name='credentialsapp_users')
    user_permissions = models.ManyToManyField(Permission, related_name='credentialsapp_users')
    

    def __str__(self):
        return self.username
