from django.db import models

# Create your models here.
class Model(models.Model):
    name=models.CharField(max_lenth=50)
    image = models.ImageField(_("Image"), upload_to=None, height_field=None, width_field=None, max_length=None)