import numpy as np
from tabulate import tabulate
import math


def x1(x2, x3):
    return (-2*x2)-(4*x3)+4


def x2(x1, x3):
    return -2*x1+x3+2


def x3(x1, x2):
    return (x1+2*x2)/4


#eps = [0.001, 0.001, 0.001]
v = [np.array([1, 2, 3])]
x = np.array([1, 2, 3])  # the initiale value of x
# 6 is the number of etirations i could not do it with 'while' 
for i in range(6): 
    v.append([x1(x[1], x[2]), x2(x[0], x[2]), x3(x[0], x[1])])
    x = v[-1] #x = the last element of the v
    print("v =", v)
    print("x =", x)
# print(v)
print(tabulate(v, headers=["n", "x1", "x2", "x3"],
    tablefmt='fancy_grid', showindex="always"))
