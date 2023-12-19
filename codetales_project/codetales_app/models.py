from django.db import models

# Create your models here.
class Registration(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)

class AdminRegistration(models.Model):
    UserName=models.CharField(max_length=25)
    Password=models.CharField(max_length=20)

class Feedback(models.Model):
    Name=models.CharField(max_length=25)
    Email=models.EmailField()
    Phone=models.CharField(max_length=10)
    Message=models.CharField(max_length=300)

class CStory(models.Model):
    Level=models.IntegerField()
    Page=models.IntegerField()
    Title=models.CharField(max_length=35,blank=True)
    Content=models.TextField()

class PyStory(models.Model):
    Level=models.IntegerField()
    Page=models.IntegerField()
    Title=models.CharField(max_length=35,blank=True)
    Content=models.TextField()

class CPuzzle(models.Model):
    puzzleID=models.IntegerField()
    puzzleTitle=models.CharField(max_length=25)
    puzzleContent=models.CharField(max_length=1000)
    puzzleInstructions=models.CharField(max_length=1000)
    puzzleConditions=models.CharField(max_length=1000)

class PyPuzzle(models.Model):
    puzzleID=models.IntegerField()
    puzzleTitle=models.CharField(max_length=25)
    puzzleContent=models.CharField(max_length=1000)
    puzzleInstructions=models.CharField(max_length=1000)
    puzzleConditions=models.CharField(max_length=1000)

class CChallenge(models.Model):
    challengeID=models.IntegerField()
    challengeTitle=models.CharField(max_length=25)
    challengeContent=models.CharField(max_length=1000)
    challengeInstructions=models.CharField(max_length=1000)
    challengeConditions=models.CharField(max_length=1000)

class PyChallenge(models.Model):
    challengeID=models.IntegerField()
    challengeTitle=models.CharField(max_length=25)
    challengeContent=models.CharField(max_length=500)
    challengeInstructions=models.CharField(max_length=500)
    challengeConditions=models.CharField(max_length=500)