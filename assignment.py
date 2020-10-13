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
    a=float(a)
    b=float(b)
    ca= convertAngle(ca)

    if oppositeSide == "True":
        x1 = (a**2 + b**2) - (2*a*b*math.cos(ca))
        c=math.sqrt(x1)
        return c

    elif oppositeSide == "False":
        if a>b:
            a1 = 1
            b1 = (2*b*math.cos(ca))
            c1 = b**2 - a**2
            q = quadratic(a1,b1,c1)
            return q
            
        if b>a:
            a1 = 1
            b1 = (2*a*math.cos(ca))
            c1 = a**2 - b**2
            q = quadratic(a1,b1,c1)
            return q




    

def convertAngle(deg):
    deg = float(deg)
    rad=(deg*math.pi)/180
    return rad

def solution(solutions):
    sort.solutions()
    x2 = solutions[1]
    return x2
    

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


print(solution([-8.9, 5.3])