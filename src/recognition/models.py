from django.db import models

# Create your models here.


class FaceImage(models.Model):
    face = models.ImageField(upload_to='user_images')


class UserImages(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.PROTECT)
    images = models.ManyToManyField(FaceImage)
