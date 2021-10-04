from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import User

import io

from .serializers import UserSerializer

Users = get_user_model()

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = Users.object.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class ListUserView(generics.ListAPIView, generics.mixins.ListModelMixin):
    queryset = User.object.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )


