import amino
import os
import time
import getpass
os.system("clear")

green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;93m"
none = "\033[0m"






def Tass2(data):
        listusers=[]
        for userId ,status in zip(data.userId,data.status):
                if status !=9 and status !=10:
                        listusers.append(userId)

def Tass(data):
        listusers=[]
        for userId ,status in zip(data.profile.userId,data.profile.status):
                if status !=9 and status !=10:
                        listusers.append(userId)
os.system('clear')
client=amino.Client()

e = input (yellow+" your email : ")
print(none+'—'*30)

a = input (yellow+" password : ")
client.login(email=e,password=a)
print("       ")
print("—"*30)
infoos = input ("url of your profile: ")
infoo=amino.Client().get_from_code(infoos)
chatId=infoo.objectId
comId=infoo.path[1:infoo.path.index("/")]


subclient = amino.SubClient(comId=comId, profile=client.profile)


o = input('the comment : ')


oldComments = []
listusers = subclient.get_all_users(start=1,size=2000)
for nickname, id in zip(listusers.profile.nickname, listusers.profile.userId):
    wallComments = subclient.get_wall_comments(str(id), sorting='top').content

    if o not in wallComments:
       oldComments.append(listusers)
       subclient.comment(o,userId=id)
       print(green+"Commented on", nickname,id)