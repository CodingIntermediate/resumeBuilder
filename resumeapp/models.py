from django.db import models
# Create your models here.
# this model is created for companies
class RegModel(models.Model):
    regid=models.AutoField(primary_key=True)
    Organization_Category=models.CharField(max_length=100)
    Business_Name=models.CharField(max_length=100)
    Address=models.TextField(max_length=100)
    States=models.CharField(max_length=100)
    Cities=models.CharField(max_length=100)
    Pincode=models.IntegerField(null=True)
    Number=models.IntegerField(null=True)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=100)
    Status=models.CharField(default='0',max_length=5)
    usertype=models.CharField(max_length=100,default='company')
    
# -------------------------------------------------------------------
# this model is for users
class UserModel(models.Model):
    userid=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=50)
    Date_Of_Birth=models.IntegerField(null=True)
    Education=models.CharField(max_length=100)
    Skills=models.CharField(max_length=100)
    Conatact_Number=models.IntegerField(null=True)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,default='User')


# a model for login(Comapanies) 
class LoginModel(models.Model):
     Email=models.EmailField(unique=True)
     Password=models.CharField(max_length=100)