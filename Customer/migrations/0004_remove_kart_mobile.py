# Generated by Django 4.1.7 on 2023-03-25 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_rename_cart_kart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kart',
            name='mobile',
        ),
    ]