from django.urls import path
from . import views

app_name = "facerecognition"


urlpatterns = [
    # urls for Django Rest Framework API
    path('get_csrf', views.CSRFToken.as_view()),
    path('add_person/', views.CreatePersonView.as_view()),
    path("get_label/", views.GetIdView.as_view()),
    path('add_temp_person/', views.CreateTempPersonView.as_view()),
    path('batch_train/', views.BatchRecognition.as_view())

]
