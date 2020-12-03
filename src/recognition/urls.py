from django.urls import path, include
from rest_framework import routers

from . import views

recognition = 'src.recognition'

router = routers.DefaultRouter()

urlpatterns = [
    path("recognize-face", views.FaceRecognitionView.as_view()),
    path("save-face", views.SaveFaceView.as_view()),
    path("train-face", views.TrainerView.as_view())
]

urlpatterns += ()
