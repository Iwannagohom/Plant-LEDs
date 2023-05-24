import wifi
import socketpool
import ssl
import adafruit_requests
import time
import microcontroller
import json
from ledPixelsPico import *

pix = ledPixels(64, board.GP0)
pix1 = ledPixels(64, board.GP15)


def timeToSeconds(t, k=-5):               #(t= "12:59:18 AM")
    #print(t)
    h,m,s = t.split(":")

    
    s,tt=s.split(" ")

    h=int(h)                       
    m=int(m)                        
    s=int(s)                        
    #print(h,m,s,tt)


    if h == 12 and tt == "AM":
        nH = 0
    else:
        nH = h*60*60
    
    
    nM=m*60
    
    #print(h, "-->", nH)
    #print(m, "-->", nM)
    
    #print(nH,nM, s, tt)

    total = nH + nM + s
    #print("Total =", total, tt)
    
    if total < 18000:
        total = ((total + 86400)+k*60*60)
        #print("Total = ", total, tt)
    
    return total
    


wifi.radio.connect("TFS Students", "Fultoneagles")
print("connected")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
print("My IP address is", wifi.radio.ipv4_address)


url = "http://makerspace.local/makerspaceTime.php"

response = requests.get(url)
print(response.text)

t=json.loads(response.text)
response.close()

for key in t.keys():
    print(key, t[key])
    
#print(".....", t["tm_hour"], t["tm_min"], t["tm_sec"])






urlS = "https://api.sunrise-sunset.org/json?lat=38.6631&lng=-90.5771"
response = requests.get(urlS)
print("!!!!!!!!!!",response.text)
t=json.loads(response.text)
response.close()


rise = (t["results"]["sunrise"])
setd = (t["results"]["sunset"])


def Curent(t):
    ch = t["tm_hour"]				#curent (time) hours.
    cm = t["tm_min"]
    cs = t["tm_sec"]

    cH = ch*60*60					#curent (time) hours in Seconds.
    cM = cm*60

    cTotal=(cH+cM+t["tm_sec"])		#Curent time in seconds

    return cTotal



while True:
    try:
        response = requests.get(url)
        t=json.loads(response.text)
        response.close()
        cTotal = Curent(t)
        #print(cTotal)
        #print(response.text)
        time.sleep(1)
        pix1.brightness=0.1
        pix.brightness=0.1

        #St Louise
        if cTotal > (timeToSeconds(rise, -5)) and cTotal < (timeToSeconds(setd, -5)):
            pix.rainbow()
            pix.brightness=0.1
            #pix.clear()
        else:
            #pix.rainbow()
            pix.clear()
            print("Night")
            
            
            
            #Kyiv
        if cTotal > (timeToSeconds(rise, 2))  and cTotal < (timeToSeconds(setd, 2)):
            pix1.rainbow()
            #pix.clear()
            pix1.brightness=0.1
        else:
            #pix1.rainbow()
            pix1.clear()
            print("Night")
            
    except Exception as e:
        print("error:", e)
        time.sleep(2)

        
