import math
def mvolume(r,h):
    z= (1/3) * math.pi * math.pow(r,2)*h
    return z


vsize=mvolume(4,7)
print(vsize)