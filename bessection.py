import math
from tabulate import tabulate
fun = lambda x: math.exp(x)-(2*((x)**2))
def bess(a,b):
    if (fun(a)*fun(b)>=0):
        print("\n We can't solve this equation !")
        return
    e = 0.001
    n = round(math.log2((b-a)/e)/math.log2(2))
    deltaX = b - a
    c = (b + a)/2
    i = 0
    info = [["a", "b", "c", "f(a)", "f(b)", "f(c)", "deltaX"],
             [round(a, 5), round(b, 5), round(c, 5), round(fun(a), 5), round(fun(b), 5), round(fun(c), 5),
              round(deltaX, 5)]]

    while (deltaX>e and i<=n):
        if (fun(c) == 0.0):
            break
        if(fun(a)*fun(c)<0):
            b=c
        else:
            a=c
        c = (b + a) / 2
        deltaX = b - a
        i = i + 1
        info.append([round(a, 5), round(b, 5), round(c, 5), round(fun(a), 5), round(
            fun(b), 5), round(fun(c), 5), round(deltaX, 5)
                      ])
    print("the root is : ",c)
    print(tabulate(info, headers='firstrow', tablefmt='fancy_grid'))

bess(1, 2)