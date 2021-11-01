from django.urls import path
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

# router.register(r'product', ProductView)
router.register(r'category/admin', CategoryViewAPI, basename='category-admin')

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/crud/', ProductCRUDLView.as_view()),
]

urlpatterns += router.urls
