import os
import base64
from PIL import Image
import cv2
import numpy

from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.core.files.base import ContentFile
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
    def post(self, request):
        face = request.POST.get('face')
        if face:
            format, imgstr = face.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # You can save this as file instance.
            print(data)
            pil_img = Image.open(data).convert('RGB')

            print(pil_img)
            img = numpy.array(pil_img)
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

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            return JsonResponse({"status": True, "message": "Image Received.", "data": {"confidence": confidence, "name": id}})
        else:
            return JsonResponse({"status": False, "message": "Face Base64 not provided.", "data": []})


class TrainerView(APIView):
    def post(self, request):
        pass


class saveFace(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.user)
        return JsonResponse({'status': True, "message": "Face Saved", "data": {"user": request.user.username}})


class createUser(APIView):
    def post(self, request):
        pass
