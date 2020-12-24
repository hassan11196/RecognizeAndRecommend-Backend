import os
import base64
from PIL import Image
import cv2
import numpy as np
import time

from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from .models import FaceImage, UserImageSet
from .business import create_user, label_image

# Create your views here.
recognizer = cv2.face.LBPHFaceRecognizer_create()
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
print(CURRENT_FOLDER + '/trainer/trainer.yml')
recognizer.read(CURRENT_FOLDER + '/trainer/trainer.yml')
cascadePath = CURRENT_FOLDER + "/cascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

names = ['None', 'Hassan', 'areeba']
minW = 0.1 * 100
minH = 0.1 * 100


class FaceRecognitionView(APIView):
    parser_classes = (JSONParser, )

    def post(self, request):
        face = request.data.get('face')
        if face:
            format, imgstr = face.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # You can save this as file instance.

            print(data)
            id = label_image(image=data)
            print(id)
            if (id != 'unknown'):
                print(id)
                user_image_set = UserImageSet.objects.filter(id=id).first()
                if not user_image_set:
                    id = "Hassan"
                    auth_token = 'DONT_USE_THIS_USER'

                else:
                    id = user_image_set.user.username
                    auth_token = str(user_image_set.user.auth_token)
                    print(auth_token)

                return JsonResponse({
                    "status": True,
                    "message": "Image Received.",
                    "data": {
                        "name": id,
                        "auth_token": auth_token
                    }
                })

            else:
                id = "unknown"

                return JsonResponse({"status": True, "message": "Image Received.", "data": {"name": id}})

        else:
            return JsonResponse({"status": False, "message": "Face Base64 not provided.", "data": {}})


class TrainerView(APIView):
    def post(self, request):
        print(request.user)
        user = request.user
        user_image_set, created = UserImageSet.objects.get_or_create(user=user)
        if created:
            return JsonResponse({'status': False, "message": "No Face Images for User", "data": {"user": request.user.username}})
        faceSamples = []
        ids = []
        for image in user_image_set.images.all():
            pil_img = Image.open(image.face).convert('L')

            print(pil_img)
            img_numpy = np.array(pil_img, 'uint8')
            # Convert RGB to BGR
            faceSamples.append(img_numpy)
            ids.append(user_image_set.id)
            print(ids)

        recognizer.update(faceSamples, np.array(ids))
        recognizer.write(CURRENT_FOLDER + '/trainer/trainer.yml')

        return JsonResponse({"status": True, "message": "Model Re-Trained for face.", "data": {"name": user.username}})


class SaveFaceView(APIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = (JSONParser, )

    def post(self, request):
        print(request.user)
        face = request.data.get('face')
        username = request.data.get('username')
        if face:
            format, imgstr = face.split(';base64,')
            ext = format.split('/')[-1]
            file_name = f'{request.user.username}.{int(time.time())}'
            data = ContentFile(base64.b64decode(imgstr), name=file_name + ext)  # You can save this as file instance.
            print(data)

            result = create_user(username, data)

            return result
        else:
            return JsonResponse({"status": False, "message": "Face Base64 not provided.", "data": []})


class CreateFaceView(APIView):
    parser_classes = (JSONParser, )

    def post(self, request):

        face = request.data.get('face')
        username = request.data.get('username')
        if face:
            format, imgstr = face.split(';base64,')

            ext = format.split('/')[-1]
            file_name = f'{request.user.username}.{int(time.time())}'
            data = ContentFile(base64.b64decode(imgstr), name=file_name + ext)  # You can save this as file instance.
            print(data)

            result = create_user(username, data)

            return JsonResponse(result)
        else:
            return JsonResponse({"status": False, "message": "Face Base64 not provided.", "data": []})