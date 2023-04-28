import board
import neopixel
from ledPixelsPico import *

#Black = Red, Blue = Purple, White = Gray
#purple = gp0, gray = gnd, black = vbu.


pix = ledPixels(64, board.GP0)
print("running")
pix.clear()


def lightAll (r,g,b):
    for i in range(64):
        pix.light(i,(r,g,b))
        

    




lightAll(20,0,20)

