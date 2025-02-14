from django.db import models

# Create your models here.

class ContactDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=500,null=True,blank=True)

