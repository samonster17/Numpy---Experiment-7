import numpy as np
#start at 0
a = 0
b = 0
A = np.empty(())

while a <= 99:
    a+=1
    #mult by 2
    b=a**2
    A = np.append(A,b)
    if a ==100:
        A.resize((10,10))
    #modulus 
    c = A[A%3==0]
    
    np.save('div_by_3.npy', c)