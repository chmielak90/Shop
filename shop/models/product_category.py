from django.db import models


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=32)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.category_name
