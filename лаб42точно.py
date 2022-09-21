import math
def func1(x1,x2,x3,x4):
    z=2.33*math.pi*(x1*math.sin(x2)+x2*math.cos(x3)) + math.pow(math.e,x3*x4)
    return(z)
x=float(input("x:"))
y=float(input("y:"))
c=float(input("c:"))
d=float(input("d:"))
z=func1(x,y,c,d)
print(z)