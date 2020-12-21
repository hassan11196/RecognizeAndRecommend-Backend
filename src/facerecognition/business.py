from .db import * 
import copy 
import face_recognition
import cv2
import pickle
import os.path
import numpy as np
from .models import TempPerson
directory = os.path.dirname(__file__)


def create_user(request):
    number = -1
    if(request.POST['name']):
        name = request.POST['name']
    else:
        name="person"
    number = compare_user_names(name)

    if not encode_images(request.FILES['image'],(name+ "." +str(number))):
        status = {"status":False,"message":"Unable To Detect Face In Image."}
        return status
    status = add_user(request.FILES['image'],number+1,name)
    return status


def create_temp_user(request):
    if(request.POST['name']):
        name = request.POST['name']
    else:
        name="person"

    status = add_temp_user(request,name)
    return status


def encode_images(image,name):
    if os.path.isfile(os.path.join(directory,'../../facedump/face_names')):
        file = open(os.path.join(directory,"../../facedump/face_names"),'rb')
        known_face_names = pickle.load(file)
        file.close()
        file = open(os.path.join(directory,'../../facedump/face_encoding'),'rb')
        known_face_encodings = pickle.load(file)
        file.close()
    else:
        known_face_names = []
        known_face_encodings = []
    if image is not None:
        image =face_recognition.load_image_file(image)
        enc = face_recognition.face_encodings(image)
        if len(enc) !=0:
            known_face_encodings.append(enc[0]) 
            known_face_names.append(str(name))
            file = open(os.path.join(directory,"../../facedump/face_names"),'wb')
            pickle.dump(known_face_names,file)
            file.close()
            file = open(os.path.join(directory,"../../facedump/face_encoding"),'wb')
            pickle.dump(known_face_encodings,file)
            file.close()
            return True
        else:
            return False 


def batch_image_train():
    TempPersons = TempPerson.objects.all()
    if len(TempPersons)>0:
        for person in TempPersons:
            print(person)
            name = person.name
            image = person.image
            number = compare_user_names(name)
            if encode_images(image,(name+ "." +str(number))):
                add_user(image,number+1,name)
            person.delete()


            





def label_image(request):
    if not request.FILES['image']:
        return {"status":False,"message":"Invalid Parameters"}
    frame = request.FILES['image']
    frame =face_recognition.load_image_file(frame)
    file = open(os.path.join(directory,"../../facedump/face_names"),'rb')
    known_face_names = pickle.load(file)
    file.close()
    file = open(os.path.join(directory,'../../facedump/face_encoding'),'rb')
    known_face_encodings = pickle.load(file)
    file.close()
    face_locations = []
    face_encodings = []
    face_names = []
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.45)
        name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
        else:
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        face_names.append(name)
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4

    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    #     # Draw a label with a name below the face
    #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    #     font = cv2.FONT_HERSHEY_DUPLEX
    #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 3.0, (255, 255, 255), 4)
    if len(face_names) == 1:
        if(face_names[0] == 'Unknown'):
            return {"status": True,
            "message": "Image Received.",
            "data": {
                "confidence": 0,
                "name": face_names,
                "auth_token": None
            }}
        else:
            return {"status": True,
            "message": "Image Received.",
            "data": {
                "confidence": 100,
                "name": face_names,
                "auth_token": None
            }}

    return {"status": True,
            "message": "Image Received With Multiple Faces.",
            "data": {
                "confidence": 100,
                "name": face_names,
                "auth_token": None
            }}       