#! python3

import math

def tempConversion(degrees, unit="C"):
    if unit =="C":
        f= (degrees*(9/5))+32
        f= float(f)
        f = round(f, 1)
        return f
    elif unit == "F":
        c = (degrees-32)*(5/9)
        c=float(c)
        c = round (c, 1)
        return c


def factorPair(a,b):
    #inputs
    #a=number
    #b=factor
    #returns b and factor that equals to a
    a = int(a)
    b = int(b)
    c = a/b
    c=int(c)
    factors = [b,c]
    factors.sort()
    return factors

def cosineLaw(a,b,c, oppositeSide= "True"):
    #inputs 
    #a,b are the sides 
    #c=angle


    

def convertAngle():
    pass

def solution():
    pass

def quadratic():
    pass
