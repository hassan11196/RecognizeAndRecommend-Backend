from ..users.models import User
from src.users.models import User
from django.shortcuts import get_object_or_404
import datetime

# def compare_user_names(name):
#     exist = User.objects.filter(username = name).last()
#     if(exist):
#         print(exist.username)
#         return int(exist.username.split('.')[1])
#     else:
#         return 0


def add_user(image, username, uuid):

    # try:
    if User.objects.filter(username=username).exists():
        return {"status": True, "message": "Username Already Exists, please choose new username", "username": username}

    user = User.objects.create(profile_picture=image, username=username, id=uuid)
    print("User Created")
    print(user)

    status = {
        "status": True,
        "message": "Person Has Been Added",
        "data": {
            "username": username,
            "auth_token": str(user.auth_token)
        }
    }
    return status
    # except:
    #     status = {"status":False,"message":"Unable To Add Person"}
    #     return status


# def add_temp_user(request,name):
#     TempPerson.objects.create(name=name,image=request.FILES['image'])
#     status = {"status": True, "message":"Person Has Been Added To Temporary Storage For Batch Process"}
#     return status

# def get_auth_token(name):
#     try:
#         user = User.objects.get(username=name)
#         token = str(user.auth_token)
#     except:
#         token = "DONT_USE_THIS_USER"
#     return token
