from microbit import *
import neopixel
from random import randint
import math

MAX_X = 12
MAX_Y = 5
LED_COUNT = 59
LED_PIN = pin0
STRIP = neopixel.NeoPixel(LED_PIN, LED_COUNT+1)
SENSE = 20

class Dot():
    def __init__(self):
        pass

def transform(x,y):
    #grid x/y is 12/5
    x = x % MAX_X
    y = y % MAX_Y
    s = x * MAX_Y   #strip
    if (x/2 == x//2) | (x == 0):   #x is even -> y(0-4) 
        s += y
        #s += 4-y 
    else:                          #x is odd ->y(4-0)
        s += MAX_Y-1-y
        #s += y
    return s
def wheel(pos):
    pos = pos & 255
    if pos < 85:
        return (pos, 255 - pos, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos, 0, pos)        
    else:
        pos -= 170
        return (0, pos , 255 - pos)

def display_heart(strip):
    heart = ((2,0),(1,1),(2,1),(3,1),(0,2),(1,2),(2,2),(3,2),(4,2),(0,2),(1,2),(2,2),(3,2),(4,2),(1,4),(3,4))
    for x in range(0,len(heart)):
        x = heart[x][0]
        y = heart[x][1]
        s = transform(x,y)
        strip[s] = (125,0,125)
        strip.show()
        sleep(500)

if __name__ == '__main__':
    
    while True:
        STRIP.clear()
        display_heart(STRIP)
