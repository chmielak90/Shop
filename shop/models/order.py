from django.db import models

from shop.models.address import Address
from shop.models.user import User


class Order(models.Model):
    user = models.ForeignKey(User)

    comments = models.TextField(null=True,
                                verbose_name='Comment to order',
                                blank=True)
    sum_product_cost = models.FloatField(null=False)
    send_address = models.OneToOneField(Address)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "user: {}, order num: {}".format(self.user, self.id)
