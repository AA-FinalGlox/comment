import amino
import os;
import time
import getpass
os.system("clear")
zero = 0
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

green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;93m"
none = "\033[0m"

e = input (yellow+"#your email: ")
a = input (yellow+"#password: ")
client.login(email=e,password=a)
while (True):
	os.fork()
infoos = input ("url of your profile: ")
infoo=amino.Client().get_from_code(infoos)
chatId=infoo.objectId
comId=infoo.path[1:infoo.path.index("/")]

subclient = amino.SubClient(comId=comId, profile=client.profile)

i = input(green+'Maximum? : ')
o = input(green+'comment : ')

while zero < 10:
    oldComments = []
    listusers = subclient.get_online_users(start=0,size=i)
    for nickname, id in zip(listusers.    profile.nickname, listusers.profile.userId):
        wallComments = subclient.    get_wall_comments(str(id), sorting='top').content

    if o not in wallComments:
        oldComments.append(listusers)
        subclient.comment(o,userId=id)
        print(green+"Commented on",none+nickname,id)

    time.sleep(10.0)
