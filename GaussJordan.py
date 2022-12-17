import  numpy as np
ab = np.array([[1.0, 2.0, 4.0, 4.0],
                [2.0, 1.0, -1.0, 2.0],
                [1.0, 2.0, -4.0, 0.0]],
                float) 
n = ab.ndim + 1
print("matrix betfore elemenation")
print(ab)  
# Jordan elemenation 
for i in range(n):
    for j in range(n):
        if (i == j):
             pass
        else : 
            fector = ab[j][i]/ab[i][i]
            for k in range(n+1):
                ab[j][k] = ab[j][k] - fector * ab[i][k]
print("matrix after elemenation")
print(ab)                
# Displaying solution    
print('\nSolutions are: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
