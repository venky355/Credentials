# Generated by Django 5.0.3 on 2024-04-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Credentialsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=2083),
        ),
    ]
