from curses import meta
import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class users_manager(BaseUserManager):
    def create_superuser(self, email, name, password=None):
        User.objects.create(
            email = self.normalize_email(email),
            name = name,
            password = make_password(password)
        )

class User(AbstractBaseUser):
    name = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=35, null=False, blank=False, unique=True)
    password = models.CharField(max_length=1024, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = users_manager()

