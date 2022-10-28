import numpy as np
import sys

n = int(input('Enter number of unknowns: '))

a = np.zeros((n,n+1))

x = np.zeros(n)

print('Enter the Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

print(a)
#Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Eurore : can not divide by zero!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            
            a[j][k] = a[j][k] - ratio * a[i][k]
            
print("the matrix after elimination : ")
print(a)


x[n-1] = a[n-1][n]/a[n-1][n-1]# this is the last solution : xn

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        print(j)
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Displaying all the solutions
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')