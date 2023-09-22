from django.db import models

# Create your models here.
class Registration(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
