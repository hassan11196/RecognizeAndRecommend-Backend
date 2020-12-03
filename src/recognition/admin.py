from django.contrib import admin

from .models import FaceImage, UserImageSet
# Register your models here.
admin.site.register(UserImageSet)
admin.site.register(FaceImage)