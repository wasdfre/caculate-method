# -*- coding: utf-8 -*-

import numpy as np

N=100000


x=[]
for k in range(0,N):
    x.append(1/N*k)


dx=[]#使用空数组
y=[]

for k in range(0,N-1):
    y.append(np.exp(x[k]))
    dx.append(x[k+1]-x[k])

x=np.matrix(x)#矩阵化
y=np.matrix(y)
dx=np.matrix(dx)


I_num=np.sum(np.multiply(y,dx))
#I_num=np.dot(y,dx.transpose(),)[0,0]

I_exact=np.e-1

error=np.abs(I_exact-I_num)

print('I_exact:',I_exact)
print('I_num:',I_num)
print('error:',error)



















