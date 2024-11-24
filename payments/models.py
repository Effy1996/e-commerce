from django.db import models
import datetime
from fashion.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 

# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=250)
    shipping_email = models.EmailField(max_length=250)
    shipping_address1 = models.CharField(max_length=250)
    shipping_address2 = models.CharField(max_length=250)
    shipping_county = models.CharField(max_length=250)
    shipping_town = models.CharField(max_length=250)
    shipping_zipcode = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Shipping Addresses "

    def __str__(self):
        return f"Shipping Address - {str(self.id)}"

#create Shipping Address when user signs up
def create_shipadd(sender, instance, created, **kwargs):
    if created:
        user_shipadd = ShippingAddress(user=instance)
        user_shipadd.save()

#Automate Shipping Address
post_save.connect(create_shipadd, sender=User)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    shipping_address = models.TextField(max_length=10000, default='')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_ordered = models.DateTimeField(default=datetime.datetime.now)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Order - {str(self.id)}'

#Add Shipping date automatically
@receiver(pre_save, sender=Order)
def set_shipped_date_on_update(sender, instance, **kwargs):
	if instance.pk:
		now = datetime.datetime.now()
		obj = sender._default_manager.get(pk=instance.pk)
		if instance.shipped and not obj.shipped:
			instance.date_shipped = now



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'Order Item - {str(self.id)}'