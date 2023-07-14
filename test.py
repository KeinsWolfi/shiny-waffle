import requests as req
import mojang
import time
from datetime import datetime


userinput = str(input("Enter the username you want to request- "))


#get uuid and save it to a var

MojangReq= req.get("https://api.mojang.com/users/profiles/minecraft/"+userinput).json()
uuid=str(MojangReq['id'])



data = req.get("https://api.hypixel.net/player?key=45e4f94d-1152-4a0c-9360-ab09828a184a&uuid="+uuid).json()
#recentgames = req.get("https://api.hypixel.net/recentgames?key=27477778-1002-491b-ab71-0a11adeb8912&uuid="+uuid).json()



timezone = input("Enter your timezone in UTC (put - if negative) >> UTC+")

firstLoginUnixw = data['player']['firstLogin']
firstLoginUnix = int(firstLoginUnixw)+int(timezone)*3600000
firstLoginP = datetime.utcfromtimestamp(float(firstLoginUnix/1000)).strftime('%Y-%m-%d %H:%M:%S')

lastLoginUnixw = data['player']['lastLogin']
lastLoginUnix = int(lastLoginUnixw)+int(timezone)*3600000
lastLoginP = datetime.utcfromtimestamp(float(lastLoginUnix/1000)).strftime('%Y-%m-%d %H:%M:%S')

lastLogoutUnixw = data['player']['lastLogout']
lastLogoutUnix = int(lastLogoutUnixw)+int(timezone)*3600000
lastLogoutP = datetime.utcfromtimestamp(float(lastLogoutUnix/1000)).strftime('%Y-%m-%d %H:%M:%S')


#print(data)
#print(recentgames)
print("PlayerKarma: "+str(data['player']['karma']))
print("First Login: "+str(firstLoginP))
print("Last Login: "+str(lastLoginP))
print("Last Logout: "+str(lastLogoutP))
input("Press ENTER to exit")
