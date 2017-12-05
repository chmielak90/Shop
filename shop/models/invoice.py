from django.db import models

from shop.models.address import Address
from shop.models.order import Order


class Invoice(models.Model):
    order = models.OneToOneField(Order)
    bill_address = models.ForeignKey(Address)
    inserted_date = models.DateField(auto_now_add=True)
