import requests
from django.http import HttpResponse
from rest_framework import serializers
from mainapp.models import Product
from django.core.serializers.xml_serializer import Serializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'