import requests as req
import mojang
import time
from datetime import datetime


userinput = str(input("Enter the username you want to request- "))


#get uuid and save it to a var#

MojangReq= req.get("https://api.mojang.com/users/profiles/minecraft/"+userinput).json()
uuid=str(MojangReq['id'])

#apikey

f=open('apikey.txt', 'r+')
apikey=f.read()
f.close()

data = req.get("https://api.hypixel.net/player?key=27477778-1002-491b-ab71-0a11adeb8912&uuid="+uuid).json()

firstLoginUnix = data['player']['firstLogin']
firstLoginP = datetime.utcfromtimestamp(float(firstLoginUnix/1000)).strftime('%Y-%m-%d %H:%M:%S')

lastLoginUnix = data['player']['lastLogin']
lastLoginP = datetime.utcfromtimestamp(float(lastLoginUnix/1000)).strftime('%Y-%m-%d %H:%M:%S')


#print(data)
print("PlayerKarma: "+str(data['player']['karma']))
print("First Login:"+str(firstLoginP)+"  (You may have to add or subtract some hours depending on your timezone, as this date is in UTC)")
print("Last Login:"+str(lastLoginP)+"  (You may have to add or subtract some hours depending on your timezone, as this date is in UTC)")
input("Press ENTER to exit")
