# Generated by Django 5.0.3 on 2024-04-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Credentialsapp', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
