from django.db import models

# Create your models here.
class Registration(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)

class Feedback(models.Model):
    Name=models.CharField(max_length=25)
    Email=models.EmailField()
    Phone=models.CharField(max_length=10)
    Message=models.CharField(max_length=300)

class ListTrial(models.Model):
    Story=models.CharField(max_length=300)
    Content=models.CharField(max_length=300)