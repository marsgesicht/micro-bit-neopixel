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
        #s += y
        s += MAX_Y-1-y 
    else:                          #x is odd ->y(4-0)
        #s += MAX_Y-1-y
        s += y
    return s
def wheel(pos):
    pos = pos & 255
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)        
    else:
        pos -= 170
        return (0, pos * 3 , 255 - pos * 3)

def display_image(strip):
    heart = ((2,0),(1,1),(2,1),(3,1),(0,2),(1,2),(2,2),(3,2),(4,2),(0,3),(1,3),(2,3),(3,3),(4,3),(1,4),(3,4))
    smiley = ((1,0),(2,0),(3,0),(0,1),(4,1),(2,2),(1,3),(3,3))
    _n = ((0,0),(4,0),(0,1),(4,1),(0,2),(4,2),(0,3),(4,3),(0,4),(1,4),(2,4),(3,4))
    _g = ((0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(4,1),(0,2),(3,2),(4,2),(0,3),(1,4),(2,4),(3,4))
    _o = ((1,0),(2,0),(3,0),(0,1),(4,1),(0,2),(4,2),(0,3),(4,3),(1,4),(2,4),(3,4))
    _c = ((1,0),(2,0),(3,0),(4,0),(0,1),(0,2),(0,3),(1,4),(2,4),(3,4),(4,4))
    images = (heart,_n,_g,_o,_c,heart,smiley)
    for k in range(len(images)):
        #sleep(500)
        strip.clear()
        image = images[k]
        for j in range(256):
            for i in range(len(image)):
                x = image[i][0]
                y = image[i][1]
                s = transform(x,y)
                strip[s] = wheel((int(i * 256 / len(image) + j*5)))
            strip.show()
def spin(strip, iteration=10):
    strip.clear()
    for i in range(iteration):
        for x in range(MAX_X):
            for y in range(MAX_Y,0,-2):
                s = transform(x,y)
                strip[s] = wheel((int(x * 256 / MAX_X + y*15)))
                strip.show()
                sleep(30)   

if __name__ == '__main__':
    (x_init,y_init,z_init) = accelerometer.get_values()
    while True:
        (x_,y_,z_) = accelerometer.get_values()
        if (x_init-15>x_) | (x_init+15<x_) | (y_init-15>y_) | (y_init+15<y_) | (z_init-15>z_) | (z_init+15<z_):
            display.clear()    
            display_image(STRIP)
            (x_init,y_init,z_init) = accelerometer.get_values()
            break
        spin(STRIP)
        
        
        
        
        
        
        
        
        
        
        