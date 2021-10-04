import io
import json


from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from mainapp.models import Product
from .serializers import *
import requests

# Create your views here.


class ProductView(generics.ListAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    permission_classes = []
    # authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    """ We have to use this method for mixins.CreateModelMixin because this mixin does not work 
    without post(create) method """


    @staticmethod
    def post(request, *args, **kwargs):
        """ we took date from other project """
        payload = {'id':'name'}
        info = requests.get('http://127.0.0.1:5000/api/category/').json()
        print(info[0].get('name'))

        title = request.POST.getlist('title')
        description = request.POST.getlist('description')
        price = request.POST.getlist('price')
        image = request.POST.getlist('image')

        product_obj = Product()

        product_obj.name = title[0]
        product_obj.description = description[0]
        product_obj.price = price[0]
        product_obj.image = image[0]

        product_obj.save()

        return redirect('http://127.0.0.1:8000/api/product/')

    # @staticmethod
    # def get(request, *args, **kwargs):
    #     info = requests.get('http://127.0.0.1:5000/api/category/')
    #     print(info.json())
    #     return HttpResponse(info.json())


""" If we use simple APIView into class we have to add get method because this method needs to see data """


# def get(self, request, format=None):
#     qs = Product.objects.all()
#     serializer = ProductSerializer(qs, many=True)
#     return Response(serializer.data)


class ProductDetailView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    permission_classes = []
    # authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    """ We have to use this method for mixins.DestroyModelMixin because this mixin does not work 
       without delete(destroy) method """

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    """ We have to use this method for mixins.UpdateModelMixin because this mixin does not work 
       without put(update) method """

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


""" One API Endpoint for CRUDL """


class ProductCRUDLView(generics.ListAPIView,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin
                       ):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    """ There is handle version of DetailView """

    def get_object(self):
        request = self.request
        id = request.GET.get('id', None)
        queryset = self.queryset
        obj = None

        if id is not None:
            obj = get_object_or_404(queryset, id=id)
            self.check_object_permissions(request, obj)
        return obj

    """ Get function """

    def get(self, request, *args, **kwaargs):
        id = request.GET.get('id', None)
        if id is not None:
            return self.retrieve(request, *args, **kwaargs)
        return super().get(request, *args, **kwaargs)

    """ Update function """

    def put(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        if id is not None:
            return self.update(request, *args, **kwargs)
        return super().update(request, *args, **kwargs)

    """ Delete function """

    def delete(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        if id is not None:
            return self.destroy(request, *args, **kwargs)
        return super().destroy(request, *args, **kwargs)
