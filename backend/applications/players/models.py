from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
