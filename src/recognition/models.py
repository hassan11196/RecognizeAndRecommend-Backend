from django.db import models

# Create your models here.


class FaceImage(models.Model):
    face = models.ImageField(upload_to='user_images')
    file_name = models.CharField(max_length=256, default="face")

    def __str__(self):
        return self.file_name


class UserImageSet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField('users.User', on_delete=models.PROTECT)
    images = models.ManyToManyField(FaceImage)

    def __str__(self):
        return self.user.username
