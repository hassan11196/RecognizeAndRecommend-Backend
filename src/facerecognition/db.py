from .models import Person,TempPerson
import datetime
def compare_user_names(name):
    exist = Person.objects.filter(name = name).last()
    if(exist):
        print(exist.username)    
        return int(exist.username.split('.')[1])
    else:
        return 0

def add_user(image,number,name):
    username = name+ "." +str(number)
    # try:
    Person.objects.create(username = username,name=name,image=image)
    status = {"status": True, "message":"Person Has Been Added","username":username}
    return status
    # except:
    #     status = {"status":False,"message":"Unable To Add Person"}  
    #     return status


def add_temp_user(request,name):
    TempPerson.objects.create(name=name,image=request.FILES['image'])
    status = {"status": True, "message":"Person Has Been Added To Temporary Storage For Batch Process"}
    return status