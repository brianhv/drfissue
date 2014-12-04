from django.db import models
from django.contrib.auth.models import User

class ContactInfo(models.Model):
    city = models.CharField(max_length=50)
    user = models.ForeignKey(User, unique=True)
