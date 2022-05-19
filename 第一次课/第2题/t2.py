# -*- coding: utf-8 -*-

import numpy as np
import time


def Factorial(n):
    global y
    y=[]
    f(n)
    return y
#    f(n)


def f(n):
    
    if n==1:
        z=1
    else:
        z=n*f(n-1)

    y.append(z)
    return z

############################################################

T1=int(2e6)
T2=int(1e4)

time0=time.time()




n1=1e10
for j in range(1,T1):
    e1=(1+1/n1)**n1

time1=time.time()


############################################################
n2=9

for j in range(1,T2):
    ff=Factorial(n2)
    e2=1
    for k in range(0,n2):
       e2=e2+1/ff[k]; 

time2=time.time()


############################################################

print('cputime1:',time1-time0)
print('e1',e1)
print('error1',np.abs(np.e-e1))

print('\n')

print('cputime2',time2-time1)
print('e2',e2)
print('error2',np.abs(np.e-e2))





