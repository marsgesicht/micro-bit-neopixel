MAX_X = 12
MAX_Y = 5

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
def test():
    for x in range(0,12):
        for y in range(0,5):
            print(x,y,transform(x,y),end="  ")
