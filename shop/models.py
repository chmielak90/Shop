from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    telephone = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)


class Address(models.Model):
    city = models.CharField(max_length=64, null=False)
    zip_code = models.CharField(max_length=32, null=False)
    street = models.CharField(max_length=64, null=False)
    house_no = models.CharField(max_length=32, null=False)
    flat_no = models.CharField(max_length=32, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}, {} {}'.format(self.zip_code, self.city, self.street, self.house_no)


class Order(models.Model):
    user = models.ForeignKey(User)

    comments = models.TextField(null=True, verbose_name='Comment to order', blank=True)
    sum_product_cost = models.FloatField(null=False)
    send_address = models.OneToOneField(Address)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "user: {}, order num: {}".format(self.user, self.id)


class Invoice(models.Model):            # faktura
    order = models.OneToOneField(Order)
    bill_address = models.OneToOneField(Address)
    inserted_date = models.DateField(auto_now_add=True)


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Shoping cart user: {}".format(self.user.username)


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=32)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField(null=False)
    category = models.ManyToManyField(ProductCategory)
    image = models.ImageField(max_length=64, blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    promo = models.NullBooleanField(default=False)
    promo_percent = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class OrderLine(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(null=False)
    price_quantity = models.FloatField(null=False)
    order = models.ForeignKey(Order, null=True, blank=True)
    shopping_cart = models.ForeignKey(ShoppingCart)


class Payment(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    order = models.OneToOneField(Order)


class ProductAvailability(models.Model):
    quantity = models.IntegerField()
    product = models.OneToOneField(Product)


# psycopg2
# blank = true