from django.urls import path, include
from rest_framework import routers

from . import views

recognition = 'src.recognition'

router = routers.DefaultRouter()

urlpatterns = [path("face", views.FaceRecognitionView.as_view())]

urlpatterns += ()
