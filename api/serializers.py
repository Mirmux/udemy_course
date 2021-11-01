import requests
from django.http import HttpResponse
from rest_framework import serializers
from mainapp.models import Product, Category
from django.core.serializers.xml_serializer import Serializer
from rest_framework_recursive.fields import RecursiveField


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'