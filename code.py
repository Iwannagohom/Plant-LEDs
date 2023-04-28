# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
from ledPixelsPico import *

pix = ledPixels(64, board.GP0)
print("running")
pix.clear(5)
#pix.brightness=0.5
#pix.rainbowForever()
