from django.db import models

from shop.models.user import User


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Shoping cart user: {}".format(self.user.username)
