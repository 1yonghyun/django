from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
    # password = models.CharField(max_length=128)
    # username = models.TextField()
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)
    # email = models.CharField(max_length=254)
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    # date_joined = models.DateTimeField()
    # last_login = models.DateTimeField()