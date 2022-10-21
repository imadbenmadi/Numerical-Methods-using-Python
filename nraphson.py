import sympy
from tabulate import tabulate
def Nraphson():
    #declare the variable X
    x = sympy.symbols('x')
    #declare thefunctuion
    fun = (x**3)-(2*(x**2))+x-2
    #calcule the derevate of F using the sympy libarary
    fderivative = fun.diff(x)

    i=0

    x0 = 3
    #the newton refson law
    xn = x0 - fun.evalf(subs={x:x0}) / fderivative.evalf(subs={x:x0})

    deltaX = x0 - xn

    #The Presision
    e=0.001

    #The first row of the table
    tap = [["n", "x0", "xn", "dx"], [i, round(x0, 3), round(xn, 3), round(deltaX, 3)]]


    while (deltaX >= e):
        x0 = xn
        xn = x0 - fun.evalf(subs={x: x0}) / fderivative.evalf(subs={x: x0})
        deltaX = x0 - xn
        i += 1
        #append rows to the list (we'll use it to draw the table)
        tap.append([i, round(x0, 3), round(xn, 3), round(deltaX, 3)])

    print("the root is : ",round(xn))
    #draw the table using tabulate libarary
    print(tabulate(tap, headers='firstrow', tablefmt='fancy_grid'))


Nraphson()