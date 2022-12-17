import numpy as np 
from tabulate import tabulate

def f1(x2,x3): 
    return (x2-2*x3+12)/5
def f2(x1,x3):                     
    return(-3*x1+2*x3-25)/8
def f3(x1,x2): 
    return(-x1-x2+6)/4 

x01=0
x02=0
x03=0
epsilon=0.001
delta=True
info = [["x01", "x02", "x03"]]
while delta:
    x1=f1(x02,x03)
    x2=f2(x1,x03)
    x3=f3(x1,x2)
    info.append([x1, x2, x3])
    e1 = abs(x1-x01)
    e2 = abs(x2-x02) 
    e3 = abs(x3-x03)
    x01=x1
    x02=x2
    x03=x3
    delta=e1>epsilon and e2>epsilon and e3>epsilon
print('\n solution x1= ', round(x1,3),' x2= ',round(x2,3) ,' x3= ',round(x3,3))
print(tabulate(info, headers='firstrow', tablefmt='fancy_grid'))
