from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=True)
    first_name   = models.CharField(max_length=128)
    last_name    = models.CharField(max_length=128)
    email        = models.EmailField()
    phone        = models.CharField(max_length=30)
