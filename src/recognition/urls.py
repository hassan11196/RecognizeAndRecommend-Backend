from django.urls import path, include
from rest_framework import routers

from . import views

recognition = 'src.recognition'

router = routers.DefaultRouter()

urlpatterns = [path("recognize-face", views.FaceRecognitionView.as_view()), path("save-face", views.saveFace.as_view())]

urlpatterns += ()
