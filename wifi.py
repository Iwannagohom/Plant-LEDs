import wifi
import socketpool
import ssl
import adafruit_requests
import time
import microcontroller
import json

def timeToSeconds(t):               #(t= "12:59:18 AM")
    h,m,s = t.split(":")
    #print(h,m,s)

    s,tt=s.split(" ")
    #print(s)
    #print(t)
    h=int(h)                       # all = (h,m,s,t)
    m=int(m)                        # ok = float(all)
    s=int(s)                        #print(type(h))
    print(h,m,s,tt)


    if h == 12 and tt == "AM":
       nH = 0
    else:
        nH = h*60*60

    print(nH)
    nM=m*60
    print(nH,nM, s, tt)

    total = nH + nM + s
    print(total, tt)



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
    
print()

url = "https://api.sunrise-sunset.org/json?lat=38.6631&lng=-90.5771"

response = requests.get(url)
print("!!!!!!!!!!",response.text)
t=json.loads(response.text)
response.close()

rise = (t["results"]["sunrise"])
setd = (t["results"]["sunset"])
print(rise, setd)

timeToSeconds(rise)
print("!!!!")
timeToSeconds(setd)





