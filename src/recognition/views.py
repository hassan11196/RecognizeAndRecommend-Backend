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
            pil_img = Image.open(data).convert('RGB')

            print(pil_img)
            img = np.array(pil_img)
            # Convert RGB to BGR
            img = img[:, :, ::-1].copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # faces = faceCascade.detectMultiScale(
            #     img,
            #     scaleFactor=1.2,
            #     minNeighbors=5,
            #     minSize=(int(minW), int(minH)),
            # )
            confidence = None

            id, confidence = recognizer.predict(gray)
            auth_token = ''
            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                print(id)
                user_image_set = UserImageSet.objects.filter(id=id).first()
                if not user_image_set:
                    id = "Hassan"
                    auth_token = 'DONT_USE_THIS_USER'

                else:
                    id = user_image_set.user.username
                    auth_token = str(user_image_set.user.auth_token)
                    print(auth_token)

                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            return JsonResponse({
                "status": True,
                "message": "Image Received.",
                "data": {
                    "confidence": confidence,
                    "name": id,
                    "auth_token": auth_token
                }
            })
        else:
            return JsonResponse({"status": False, "message": "Face Base64 not provided.", "data": []})


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
    permission_classes = [IsAuthenticated]
    parser_classes = (JSONParser, )

    def post(self, request):
        print(request.user)
        face = request.data.get('face')
        if face:
            format, imgstr = face.split(';base64,')
            ext = format.split('/')[-1]
            file_name = f'{request.user.username}.{int(time.time())}'
            data = ContentFile(base64.b64decode(imgstr), name=file_name + ext)  # You can save this as file instance.
            print(data)

            face_obj = FaceImage(face=data, file_name=file_name)
            face_obj.save()

            user_image_set, created = UserImageSet.objects.get_or_create(user=request.user)

            if created:
                user_image_set.user = request.user

            user_image_set.images.add(face_obj)

            img_count = user_image_set.images.count()

            return JsonResponse({
                "status": True,
                "message": "Face Saved.",
                "data": {
                    "num_images": img_count,
                    "name": request.user.username
                }
            })
        else:
            return JsonResponse({"status": False, "message": "Face Base64 not provided.", "data": []})
