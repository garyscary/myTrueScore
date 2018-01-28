from django.db import models

# Create your models here
class AllUserID(models.Model):
    username = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    
class User(models.Model):
    usernames = models.ManyToManyField('AllUserID')
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100,primary_key=True,unique=True)
    