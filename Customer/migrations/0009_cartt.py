# Generated by Django 4.1.7 on 2023-03-25 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customer', '0008_delete_kart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m_cart', to='store.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
