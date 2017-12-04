from django.db import models

from shop.models.order import Order


class Payment(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    order = models.OneToOneField(Order)
