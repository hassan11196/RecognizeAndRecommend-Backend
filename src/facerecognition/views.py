from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Person
from .business import *
from django.middleware.csrf import get_token
import os
# Create your views here.

class CSRFToken(View):
    def get(self,request):
        return JsonResponse({'csrfToken': get_token(request)})


class CreatePersonView(View):
    def post(self,request):
        if(request.FILES['image'] is None):
            return JsonResponse({"status":False,"message":"Invalid Parameters"})
        # if os.stat(request.FILES['image']).st_size > 5242880:
        #     return JsonResponse({"status":False,"message":"File Too Large"})

        result = create_user(request)
        return JsonResponse(result)

class CreateTempPersonView(View):
    def post(self,request):
        if(request.FILES['image'] is None):
            return JsonResponse({"status":False,"message":"Invalid Parameters"})
        result = create_temp_user(request)
        return JsonResponse(result)


class BatchRecognition(View):
    def get(self,request):
        batch_image_train()
        return JsonResponse({"status":True,"message":"Batch Trained"})

class GetIdView(View):
    def post(self,request):
        status = label_image(request)
        return JsonResponse(status)
