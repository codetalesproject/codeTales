from django.db import models

# Create your models here.
class Login(models.Model):
    UserName=models.CharField(max_length=25)
    Password=models.CharField(max_length=20)
