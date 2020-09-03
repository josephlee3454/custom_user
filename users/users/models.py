from django.contrib.auth.models import AbstractUser 
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
  email = models.EmailField(('email address'), blank=True, unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
    return self.username
    