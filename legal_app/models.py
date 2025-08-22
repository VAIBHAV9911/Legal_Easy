from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    query=models.TextField(default="")
    date=models.DateField(default=timezone.now)

class FeedBack(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    rating=models.CharField(max_length=5,null=False)
    remarks=models.TextField(default="")
    date=models.DateField(default=timezone.now)


class User(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    password=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    profile_pic=models.FileField(upload_to="user_pic/",default="")
    date=models.DateField(default=timezone.now)

class LegalAdvisor(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    password = models.CharField(max_length=20,default="")
    phone=models.CharField(max_length=13,null=False)
    qualification=models.TextField(default="")
    skills=models.TextField(default="")
    experience=models.CharField(max_length=100,default="")
    profile_pic=models.FileField(upload_to="advisory_pic/",default="")
    service_type=models.CharField(max_length=100,null=False)
    

class Service(models.Model):
    service_type=models.CharField(max_length=100,null=False,primary_key=True)
    service_pic=models.FileField(upload_to="advisory_pic/",default="")
    service_description=models.TextField(default="")

class ClientDocument(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    advisor_email=models.CharField(max_length=50)
    document_name=models.CharField(max_length=50,null=False)
    document_description=models.TextField()
    document_pic=models.FileField(upload_to="document_file/",default="")
    date=models.DateField(default=timezone.now)