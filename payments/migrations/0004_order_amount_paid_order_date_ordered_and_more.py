# Generated by Django 5.1.1 on 2024-10-15 15:30

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0008_alter_product_price'),
        ('payments', '0003_rename_address1_shippingaddress_shipping_address1_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_address1',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_address2',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_county',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_town',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_zipcode',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fashion.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
