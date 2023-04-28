import wifi
import socketpool
import ssl
import adafruit_requests
import time
import microcontroller
import json

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

