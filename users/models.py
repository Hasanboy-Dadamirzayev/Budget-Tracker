from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    balance = models.FloatField(validators=[MinValueValidator(0)])
