import wifi
import socketpool
import ssl
import adafruit_requests
import time
import microcontroller
import json


#---Conect to Wifi----
wifi.radio.connect("TFS Students", "Fultoneagles")          #Name and Pasword of the wifi
print("connected")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
print("My IP address is", wifi.radio.ipv4_address)


#----Url to get the time of sunset and sunrise---
url = "https://api.sunrise-sunset.org/json?lat=38.6631&lng=-90.5771"
                                #Lat and Lng is latitude and longitude.
                                #The time of a specific place can be found by puting in the cordinats of that place.
                    
response = requests.get(url)
print("!!!!!!!!!!",response.text)

t=json.loads(response.text)
response.close()

for key in t.keys():
    print(key, t[key])
    
    
print("			")

rise = (t["results"]["sunrise"]).    #Spesificly looking for sunset and sunset within the big chunk of text
setd = (t["results"]["sunset"])
print(rise, setd)
print("			")

r=int(rise)
print (r)







