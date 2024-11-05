from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  

    def __str__(self):
        return self.username
    
class menu(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    picture=models.URLField()

def __str__(self):
        return self.name
    

  