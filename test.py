import requests as req
import mojang
import time


print("Write your API-Key in a file in this directory named apikey.txt (if it doesnt exist yet, create it)")
input("Press ENTER key to continue")

userinput = str(input("Enter the username you want to request- "))


#get uuid and save it to a var#

MojangReq= req.get("https://api.mojang.com/users/profiles/minecraft/"+userinput).json()
uuid=str(MojangReq['id'])

#apikey

f=open('apikey.txt', 'r+')
apikey=f.read()
f.close()

data = req.get("https://api.hypixel.net/player?key="+apikey+"&uuid="+uuid).json()

print(data)
print("PlayerKarma: "+str(data['player']['karma']))
input("Press ENTER to exit")
