# Generated by Django 5.1.1 on 2024-10-17 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0008_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
