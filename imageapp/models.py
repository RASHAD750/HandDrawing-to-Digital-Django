from django.db import models

from django.contrib.auth.models import AbstractUser
#Abstract user insted of user in case of variable users
class CustomUser(AbstractUser):
    userType=models.CharField(max_length=50)
    viewpassword=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.username
class Feedback(models.Model):
 
  feedback=models.CharField(max_length=100)
  uname=models.CharField(max_length=100)

class Registration (models.Model):
    name=models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)

class Uploadimage(models.Model):
    name=models.CharField(max_length=100)
    cat=models.CharField(max_length=100)
    dis=models.CharField(max_length=100)
    image=models.ImageField()
