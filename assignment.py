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

def cosineLaw(a,b,ca, oppositeSide= "True"):
    #inputs 
    #a,b are the sides 
    #c=angle

    if oppositeSide = "True":
        x1 = (a**2 + b**2) - (2*a*b*math.cos(ca))
        c=math.sqrt(x1)
        return c

    elif oppositeSide = "False":



    

def convertAngle(deg):
    deg = float(deg)
    rad=(deg*math.pi)/180
    return rad

def solution():
    

def quadratic(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = math.sqrt((b**2)- (4*a*c))
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    solutions = [x1,x2]
    solutions.sort()
    return solutions