from django.db import models

# Create your models here.
class Make(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/images/make', height_field=None, width_field=None, max_length=None)
    
class BodyType(models.Model):
    name= models.CharField(max_length=100)
    image = models.ImageField( upload_to='media/images/body', height_field=None, width_field=None, max_length=None)
    
class Model(models.Model):
     name= models.CharField(max_length=100)
    
