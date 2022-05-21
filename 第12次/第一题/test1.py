# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np  

#设定数量和循环序列
N=5000
b=np.random.random([N,1])

#构造矩阵与循环数列
A = np.zeros([N,N])
a0 = np.random.random([1,N])
#周期延拓
a1 = np.hstack((a0,a0))

#构造循环矩阵，为什么不从0开始？从n-m到m-1，N,N+1,
#要的就是这种结构
for k in range(0,N):
    A[k,:]=a1[0,N-k:2*N-k]
#X(m)Y(N+n-m)
x0 = np.linalg.solve(A,b)

# A(k)*X(k)=Y(K)
#使用N点FFT转到频域
Lambda = np.fft.fftn(A[:,0])
#直接来不行？
inv_lambda = np.diag(1/Lambda)
#使用IFFT转换频域
x1 = np.fft.ifftn(np.dot(inv_lambda,np.fft.fftn(b)))


#print(x0)
#print(x1)
 
print('error',np.linalg.norm(x0-x1))