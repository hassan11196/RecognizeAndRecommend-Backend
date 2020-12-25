from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    username = models.CharField("User_Name",max_length = 25,primary_key=True)
    name = models.CharField("Full_Name",max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="Images/", height_field=None, width_field=None, max_length=100)
    user = models.OneToOneField('users.User', on_delete=models.PROTECT,null=True)
    
    def __str__(self):
        return self.username


class TempPerson(models.Model):
    name = models.CharField("Full_Name",max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="TempImages/", height_field=None, width_field=None, max_length=100)
    
    def __str__(self):
        return self.name