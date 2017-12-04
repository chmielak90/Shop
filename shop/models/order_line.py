from django.db import models

from shop.models.order import Order
from shop.models.product import Product
from shop.models.shopping_cart import ShoppingCart


class OrderLine(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(null=False)
    price_quantity = models.FloatField(null=False)
    order = models.ForeignKey(Order, null=True, blank=False)
    shopping_cart = models.ForeignKey(ShoppingCart)
