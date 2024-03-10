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
    
# -------------------------------------------------------------------1
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
    Status=models.CharField(default='0',max_length=5)
    usertype=models.CharField(max_length=100,default='User')

# -------------------------------------------------------------------2
# a model for login(Comapanies and users) 
class LoginModel(models.Model):
     Email=models.EmailField(unique=True)
     Password=models.CharField(max_length=100)  
# -------------------------------------------------------------------3   
#create   a model for vacancyAdding
class VacancyModel(models.Model):
    #  foreign key have a default primary_key
    regid= models.ForeignKey(RegModel, on_delete=models.CASCADE,null=True)
    Job_Category=models.CharField(max_length=100)
    Job_Name=models.CharField(max_length=100)
    Salary=models.CharField(max_length=50)
    Job_Details=models.CharField(max_length=50)
    Last_Date_For_Application=models.CharField(max_length=50)
# -------------------------------------------------------------------4  
#create a class for jobApplication for applied users
class JobApplication(models.Model):
    application_id=models.AutoField(primary_key=True)
    job_id=models.ForeignKey(VacancyModel, on_delete=models.CASCADE,null=True)
    candidate_id=models.ForeignKey(UserModel, on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(auto_now_add=True)
    canacel=models.CharField(default='0',max_length=3)
# -------------------------------------------------------------------5 
class InterviewDetails(models.Model):
    # pk,date,interview details,
    intrw_id=models.AutoField(primary_key=True)
    date=models.DateField(auto_now_add=True)
    application_id=models.ForeignKey(JobApplication,on_delete=models.CASCADE,null=True)
    interviewDetails=models.CharField(max_length=500)