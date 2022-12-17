import numpy as np 

def x_1(x2,x3): 
    return (x2-2*x3+12)/5
def x_2(x1,x3):                     
    return(-3*x1+2*x3-25)/8
def x_3(x1,x2): 
    return(-x1-x2+6)/4 

x01=0
x02=0
x03=0
epsilon=0.001
delta=True
while delta:
    x1=x_1(x02,x03)
    x2=x_2(x1,x03)
    x3=x_3(x1,x2)
    a = abs(x1-x01)
    b = abs(x2-x02) 
    c= abs(x3-x03)
    x01=x1
    x02=x2
    x03=x3
    delta=a>epsilon and b>epsilon and c>epsilon

print('\n solution x1= ', round(x1,3),' x2= ',round(x2,3) ,' x3= ',round(x3,3))
