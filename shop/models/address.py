from django.db import models

from shop.models.user import User


class Address(models.Model):
    city = models.CharField(max_length=64, null=False)
    zip_code = models.CharField(max_length=32, null=False)
    street = models.CharField(max_length=64, null=False)
    house_no = models.CharField(max_length=32, null=False)
    flat_no = models.CharField(max_length=32, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}, {} {}'.format(self.zip_code,
                                     self.city,
                                     self.street,
                                     self.house_no)
