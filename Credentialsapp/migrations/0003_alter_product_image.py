# Generated by Django 5.0.3 on 2024-04-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Credentialsapp', '0002_remove_product_image_url_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.TextField(default=''),
        ),
    ]
