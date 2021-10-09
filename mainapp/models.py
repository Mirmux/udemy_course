from django.db import models
from django.db.models.base import ModelBase

from flowersgarden.settings import AUTH_USER_MODEL


# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.FileField(upload_to='', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class XmlModel(ModelBase):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
