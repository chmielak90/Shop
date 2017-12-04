from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telephone = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
