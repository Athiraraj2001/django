from django.db import models

# Create your models here.
class User1(models.Model):
    Fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=20)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)