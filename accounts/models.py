from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import PermissionsMixin, AbstractUser

from .manager import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin,  models.Model):
    username = models.CharField(max_length=50, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = PhoneNumberField()

    data_joined = models.DateTimeField(auto_now_add=True)

    # check User status
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # call class UserManager
    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
