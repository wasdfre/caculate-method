# -*- coding: utf-8 -*-

import time
import numpy as np
import matplotlib.pyplot as plt  


def chebyshevinterpolationcoefficients(xi,yi):
    N=xi.shape[0]-1
    c=np.ones([N+1,1])
    c[0,0]=2
    c[N,0]=2

    a=np.zeros([1,N+1])
    for k in range(0,N+1):
        for j in range(0,N+1):
            a[0,k]=a[0,k]+yi[j]*np.cos(k*j*np.pi/N)/c[j,0]

        a[0,k]=a[0,k]*2/c[k,0]/N   
            
    return a

#按定义计算
#def chebyshevinterpolation(a,x):
#    N=a.shape[1]-1
#    M=x.shape[0]
#
#    y=np.zeros(M)
#    for m in range(0,M):
#        C=np.zeros([N+1,1])
#        z=x[m]
#        for k in range(0,N+1):
#            C[k,0]=np.cos(k*np.arccos(z))
#    
#        y[m]=np.dot(a,C)
#
#    return y

def chebyshevinterpolation(a,x):
    N=a.shape[1]-1
    M=x.shape[0]

    y=np.zeros(M)
    for m in range(0,M):
        T=np.zeros([N+1,1])
        z=x[m]

        T[0,0]=1
        T[1,0]=z
        for k in range(1,N):
            T[k+1,0]=2*z*T[k,0]-T[k-1,0]
    
        y[m]=np.dot(a,T)

    return y



time0=time.time()

N=160


xi=np.array([-np.cos(j*np.pi/N)  for j in range(0,N+1)])
yi=1/(1+25*xi**2)

a=chebyshevinterpolationcoefficients(xi,yi)       #计算切比雪夫插值系数

M=10000
x1=np.array([1-2/M*(M-j) for j in range(0,M+1)])
y1=chebyshevinterpolation(a,x1)                   #计算切比雪夫插值结果


fig1 = plt.figure('fig1')
plt.plot(x1,y1)

time=time.time()-time0
#yexact=1/(1+25*xi**2) 
yexact=1/(1+25*x1**2)
error=max(abs(y1-yexact))

print('time',time)
print('error',error)



