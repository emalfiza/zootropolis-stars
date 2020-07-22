from django.db import models


class Category(models.Model):
    category_name = models.TextField(max_length=100)
    friendly_name = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=300)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
