import requests as req
import mojang
import time
from datetime import datetime


userinput = str(input("Enter the username you want to request- "))


#get uuid and save it to a var

MojangReq= req.get("https://api.mojang.com/users/profiles/minecraft/"+userinput).json()
uuid=str(MojangReq['id'])



data = req.get("https://api.hypixel.net/player?key=27477778-1002-491b-ab71-0a11adeb8912&uuid="+uuid).json()

timezone = int(input("Enter your timezone in UTC (put - if negative) >> UTC+"))

firstLoginUnix = data['player']['firstLogin']
firstLoginP = datetime.utcfromtimestamp(float((firstLoginUnix+timezone*3600)/1000)).strftime('%Y-%m-%d %H:%M:%S')

lastLoginUnix = data['player']['lastLogin']
lastLoginP = datetime.utcfromtimestamp(float((lastLoginUnix+timezone*3600)/1000)).strftime('%Y-%m-%d %H:%M:%S')

lastLogoutUnix = data['player']['lastLogout']
lastLogoutP = datetime.fromtimestamp(float((lastLogoutUnix+timezone*3600)/1000)).strftime('%Y-%m-%d %H:%M:%S')



#print(data)
print("PlayerKarma: "+str(data['player']['karma']))
print("First Login:"+str(firstLoginP))
print("Last Login:"+str(lastLoginP))
print("Last Logout:"+str(lastLogoutP))
input("Press ENTER to exit")
