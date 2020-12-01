import base64
from PIL import Image
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from django.core.files.base import ContentFile
# Create your views here.


class FaceRecognitionView(APIView):
    def post(self, request):
        face = request.POST.get('face')
        if face:
            format, imgstr = face.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # You can save this as file instance.
            print(data)
            image = Image.open(data)
            print(image)
            return JsonResponse({"status": True, "message": "Image Received.", "data": []})
        else:
            return JsonResponse({"status": False, "message": "Face Base64 not provided.", "data": []})
