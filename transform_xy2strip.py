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

def drip(strip, x=0):
    y = MAX_Y - 1
    weight = 0
    puddle_x = 0
    def puddle(x):
        puddle_x += 10
        if (puddle_x<256):
            return (0,0,(puddle_x&255))
        elif (puddle_x<512):
            return ((puddle_x-255)&255,0,(512-puddle_x)&255)
        else:
            puddle_x = 0
            return (0,0,0)
    while True:
        mo_detect(accelerometer.get_values()) 
        weight = weight + 1/randint(9,19)
        if (weight<=85):
            strip[transform(x,y)] = (int(weight*3),int(85-weight),0)
        else:
            weight=0
            for iy in range(y-1,-1,-1):
                strip[transform(x,iy+1)] = (0,0,0)
                strip[transform(x,iy)] = (int(51*iy),0,int(randint(50,180)/(iy+1)))
                strip.show()
            strip[transform(x,0)] = puddle(x)
        strip.show()
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
    images= (heart,)
    for k in range(len(images)):
        #sleep(500)
        strip.clear()
        image = images[k]
        for j in range(85):
            for i in range(len(image)):
                x = image[i][0]
                y = image[i][1]
                s = transform(x,y)
                strip[s] = wheel((int(i * 256 / len(image) + j*5)))
            strip.show()
        strip.clear()
def mo_detect(xyz_init,sense=55):  #xyz_init = accelerometer.get_values()
    s = sense
    (x_init,y_init,z_init) = xyz_init
    (x_,y_,z_) = accelerometer.get_values()
    if (x_init-s>x_) | (x_init+s<x_) | (y_init-s>y_) | (y_init+s<y_) | (z_init-s>z_) | (z_init+s<z_):
        display_image(STRIP)
        
if __name__ == '__main__':
    xyz_init = accelerometer.get_values()
    while True:
        display.clear()  
        #spin(STRIP,xyz_init)
        drip(STRIP)
        
        
        
        
        
        
        
        
        
        
        