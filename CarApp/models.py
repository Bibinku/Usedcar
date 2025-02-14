from django.db import models

# Create your models here.
class CarDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    brand=models.CharField(max_length=100,null=True,blank=True)
    model=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="Car image",null=True,blank=True)
    price = models.IntegerField(null=True, blank=True)
    gst = models.IntegerField(null=True, blank=True)
    insurance = models.IntegerField(null=True, blank=True)



class BrandDB(models.Model):
    bbrand= models.CharField(max_length=100, null=True, blank=True)
    bdescription= models.CharField(max_length=500, null=True, blank=True)



    bimage = models.ImageField(upload_to="Brand image", null=True, blank=True)



class SpecificationsDB(models.Model):
    option1=models.CharField(max_length=100,null=True,blank=True)
    option2=models.CharField(max_length=100,null=True,blank=True)
    option3=models.CharField(max_length=100,null=True,blank=True)
    option4=models.CharField(max_length=100,null=True,blank=True)
    option5=models.CharField(max_length=100,null=True,blank=True)


class FeatureDB(models.Model):
    features  = models.CharField(max_length=100, null=True, blank=True)
    Option1 = models.CharField(max_length=100, null=True, blank=True)
    Option2 = models.CharField(max_length=100, null=True, blank=True)
    Option3 = models.CharField(max_length=100, null=True, blank=True)
    Option4 = models.CharField(max_length=100, null=True, blank=True)
    Option5 = models.CharField(max_length=100, null=True, blank=True)





