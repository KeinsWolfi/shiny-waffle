import requests as req
import mojang
import time


userinput = str(input("Enter the username you want to request- "))


#get uuid and save it to a var#

MojangReq= req.get("https://api.mojang.com/users/profiles/minecraft/"+userinput).json()
uuid=str(MojangReq['id'])

#apikey

f=open('apikey.txt', 'r+')
apikey=f.read()
f.close()

data = req.get("https://api.hypixel.net/player?key=27477778-1002-491b-ab71-0a11adeb8912&uuid="+uuid).json()

#print(data)
print("PlayerKarma: "+str(data['player']['karma']))
input("Press ENTER to exit")
