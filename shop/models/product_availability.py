from django.db import models

from shop.models.product import Product


class ProductAvailability(models.Model):
    quantity = models.IntegerField()
    product = models.OneToOneField(Product)
