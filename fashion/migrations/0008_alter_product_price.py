# Generated by Django 5.1.1 on 2024-10-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0007_remove_profile_old_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
