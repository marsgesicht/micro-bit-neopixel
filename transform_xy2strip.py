from microbit import *
import neopixel
from random import randint
import math

MAX_X = 12
MAX_Y = 5
LED_COUNT = 59
LED_PIN = pin0
STRIP = neopixel.NeoPixel(LED_PIN, LED_COUNT+1)
SENSE = 50

def drip(strip, drip_count=3, drip_size=10):
    y = MAX_Y - 1
    x_list = []
    weight = 0
    puddle_x = 0
    def x_list_init(dc):
        for i in range(dc):
            x_list.append([randint(0,MAX_X-1),0])
    def puddle(w=10):
        puddle_x += w
        for i in range (MAX_X):
            p_x = math.floor(puddle_x)
            if (p_x<255):
                strip[transform(i,0)] = (0,randint(0,20),(p_x&255))
            elif (p_x<510):
                strip[transform(i,0)] = ((p_x-255)&255,randint(0,30),(512-p_x)&255)
            else:
                puddle_x = 0
                strip[transform(i,0)] = (0,0,0)
        if puddle_x == 0:
            nonlocal drip_count, drip_size
            drip_count = randint(1,10)  
            drip_size = randint(7,30)
            x_list.clear()
    while True:
        for j in range(drip_count):
            if len(x_list) == 0:
                x_list_init(drip_count)
                break
            x = x_list[j][0]
            mo_detect(accelerometer.get_values()) 
            x_list[j][1] = x_list[j][1] + (j+1)/randint(9,19)
            weight = x_list[j][1]
            if (weight<=85):
                strip[transform(x,y)] = (int(weight*3),int(85-weight),0)
            else:
                x_list[j][1] = 0
                x_list[j][0] = randint(0,MAX_X-1)
                strip[transform(x,y)] = (0,0,0)
                for iy in range(y-1,-1,-1):
                    strip[transform(x,iy+1)] = (0,0,0)
                    strip[transform(x,iy)] = (int(51*iy),0,int(randint(175,255)/(iy+1)))
                    strip.show()
                puddle(drip_size)
            strip.show()
def transform(x,y):
    x = x % MAX_X
    y = y % MAX_Y
    s = x * MAX_Y 
    if (x/2 == x//2) | (x == 0): 
        s += MAX_Y-1-y
    else:
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
    _n = ((0,0),(4,0),(0,1),(3,1),(4,1),(0,2),(2,2),(4,2),(0,3),(1,3),(4,3),(0,4),(4,4))
    _g = ((0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(4,1),(0,2),(3,2),(4,2),(0,3),(1,4),(2,4),(3,4))
    _o = ((2,0),(1,1),(2,1),(3,1),(0,2),(4,2),(0,3),(4,3),(1,4),(2,4),(3,4))
    _c = ((1,0),(2,0),(3,0),(4,0),(0,1),(0,2),(0,3),(1,4),(2,4),(3,4),(4,4))
    images = (heart,) if randint(1,88)<80 else (heart,_n,_g,_o,_c,heart,)
    for k in range(len(images)):
        strip.clear()
        image = images[k]
        s_list = []
        for j in range(45):
            for i in range(len(image)):
                x = image[i][0]
                y = image[i][1]
                s = transform(x+j,y)
                s_list.append(s)
                strip[s] = wheel((int(i * 256 / len(image) + j*5)))
            strip.show()
            sleep(50)
            for i in s_list:
                strip[i] = (0,0,0)
            s_list.clear()
        strip.clear()
def mo_detect(xyz_init):
    s = SENSE
    (x_init,y_init,z_init) = xyz_init
    (x_,y_,z_) = accelerometer.get_values()
    if (x_init-s>x_) | (x_init+s<x_) | (y_init-s>y_) | (y_init+s<y_) | (z_init-s>z_) | (z_init+s<z_):
        display_image(STRIP)
if __name__ == '__main__':
    sleep(1000)
    xyz_init = accelerometer.get_values()
    while True:
        display.clear()  
        drip(STRIP,1,25)
