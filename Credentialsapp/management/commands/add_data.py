import pandas as pd
from django.core.management.base import BaseCommand
from Credentialsapp.models import Product, Category, User
from django.conf import settings

class Command(BaseCommand):
    help = "A command to add data from an Excel file to the database"

    def add_arguments(self, parser):
        # Define command arguments
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        excel_file = options['excel_file']  # Get the path to the Excel file from command line argument
        try:
            # Read Excel file into a DataFrame
            df = pd.read_excel(excel_file)

            # Iterate through each row in the DataFrame
            for index, row in df.iterrows():
                # Get or create Category based on DataFrame data
                category, created = Category.objects.get_or_create(name=row['category_name'])

                # Get or create User based on DataFrame data
                user, created = User.objects.get_or_create(username=row['username'], defaults={'role': User.Role.USERS})

                # Create or update Product based on DataFrame data
                product_defaults = {
                    'dealer': user,
                    'country': row['country'],
                    'quantity': row['quantity'],
                    'price': row['price'],
                    'image': row['image'],  # Assuming 'image' is a column in your Excel file
                    'category': category
                }
                product, created = Product.objects.update_or_create(name=row['product_name'], defaults=product_defaults)

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Excel file not found at {excel_file}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error importing data: {e}"))
