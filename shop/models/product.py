from django.db import models

from shop.models.product_category import ProductCategory


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField(null=False)
    category = models.ManyToManyField(ProductCategory)
    image = models.ImageField(max_length=64, blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    promo = models.NullBooleanField(default=False)
    promo_percent = models.FloatField(null=True, blank=True)
    promo_price = models.FloatField(null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.promo:
            discount = (self.price * self.promo_percent)/100
            self.promo_price = self.price - discount
            super(Product, self).save(*args, **kwargs)
        else:
            self.promo_price = None
            super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name
