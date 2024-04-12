from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a category management user'

    def handle(self, *args, **options):
       
        username = input("Enter the username: ")  
        password = input("Enter the password: ")


        
        try:
            category_user = User.objects.get(username=username)
            created = False
        except User.DoesNotExist:
            
            
            category_user = User.objects.create_user(username=username, password=password)
            created = True
        
        
        category_user.dealer_details = 'Category Management User'
        category_user.save()

        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created category user: {username}'))
            self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Successfully updated category user: {username}'))
