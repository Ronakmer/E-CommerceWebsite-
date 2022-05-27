from distutils.command.upload import upload
from email.policy import default
from django.db import models    
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.utils.translation import gettext_lazy as _ Users



# Create your models here.

class signup(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    # gmail= models.CharField(max_length=30)
    # address= models.CharField(max_length=30)
    # city= models.CharField(max_length=30)
    password= models.CharField(max_length=30)

class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

def __str__(self):
    return f"{self.first_name}"

# class CustomUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']






class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    product_image =models.ImageField(upload_to="home/img")
    product_price = models.CharField(max_length=10)
    product_color1 = models.CharField(max_length=10)
    product_color2 = models.CharField(max_length=10)
    product_color3 = models.CharField(max_length=10)


    product_des = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.product_name}"






class order(models.Model):
    first_name = models.CharField(max_length=30)
    gmail= models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    number= models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    

    def __str__(self):
        return f"{self.first_name}"
   
    



