
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Мини модель user, 


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email