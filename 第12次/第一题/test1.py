# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np  
from time import time
#设定数量和循环序列
N=5000
b=np.random.random([N,1])

#构造矩阵与循环数列
A = np.zeros([N,N])
a0 = np.random.random([1,N])
#周期延拓
a1 = np.hstack((a0,a0))

#结构
for k in range(0,N):
    A[k,:]=a1[0,N-k:2*N-k]
#X(m)Y(N+n-m)
#直接解方程

time0=time();
x0 = np.linalg.solve(A,b)

# A(k)*X(k)=Y(K)
#使用N点FFT转到频域
Lambda = np.fft.fftn(A[:,0])
#转换为对角阵，array就不用转行向量了
inv_lambda = np.diag(1/Lambda)
#使用IFFT转换频域
x1 = np.fft.ifftn(np.dot(inv_lambda,np.fft.fftn(b)))
time1=time();

#直接求逆运算
#x2=np.dot(np.linalg.pinv(A),b)
#time2=time();
print("timefft",time1-time0);
#太慢了
#print("timeinv",time2-time1);
print('error',np.linalg.norm(x0-x1));