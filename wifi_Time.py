import wifi
import socketpool
import ssl
import adafruit_requests
import time
import microcontroller
import json

def timeToSeconds(t):               #(t= "12:59:18 AM")      #See timeToSeconds.py for more explanations and detail
    print(t)
    h,m,s = t.split(":")

    s,tt=s.split(" ")

    h=int(h)                       
    m=int(m)                        
    s=int(s)                        
    print(h,m,s,tt)


    if h == 12 and tt == "AM":
        nH = 0
    else:
        nH = h*60*60
    
    
    nM=m*60
    
    print(nH,nM, s, tt)

    total = nH + nM + s
    print("Total =", total, tt)
    
    if total < 18000:
        sTotal = ((total + 86400)-18000)
        print("sTotal = ", sTotal, tt)
    

#---Conect to Wifi----
wifi.radio.connect("TFS Students", "Fultoneagles")
print("connected")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
print("My IP address is", wifi.radio.ipv4_address)


#----Url to get the time---
url = "http://makerspace.local/makerspaceTime.php"          #Need to have a server to conect to, to get time information

response = requests.get(url)
print(response.text)

t=json.loads(response.text)
response.close()

for key in t.keys():
    print(key, t[key])                                      #Gives all of the information - from second to date.
    
print(".....", t["tm_hour"], t["tm_min"], t["tm_sec"])    #Lokign for specific information (hours, minutes, and second) withing a big text

ch = t["tm_hour"]				#curent (time) hours.
cm = t["tm_min"]
cs = t["tm_sec"]

cH = ch*60*60					#curent (time) hours in Seconds.
cM = cm*60

cTotal=(cH+cM+t["tm_sec"])		#Curent time in seconds
print(cTotal)




#----Url to get the time of sunset and sunrise---
urlS = "https://api.sunrise-sunset.org/json?lat=38.6631&lng=-90.5771"           #See Lat.py

response = requests.get(urlS)
print("!!!!!!!!!!",response.text)
t=json.loads(response.text)
response.close()

rise = (t["results"]["sunrise"])
setd = (t["results"]["sunset"])
print("------------------", rise, setd)

while True:                             #Asking what time is it every second
    response = requests.get(url)
    print(response.text)
    time.sleep(1)

timeToSeconds(rise)
print(" ")
timeToSeconds(setd)
