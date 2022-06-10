import numpy as np
from time import time
from GS_inv import GS_ma
from SOR_inv import SOR_ma
from jacobi_inv import J_ma

n=100;
A=-2*np.eye(n);
for i in range(0,n-1):
    A[i,i+1]=1;
    A[i+1,i]=1; 

# print(A)
b=np.matrix(np.ones((1,n))).T


X=np.linalg.solve(A,b)
time0=time();

x_jacobi=J_ma(A,b);
time1=time();

x_gaussseidel=GS_ma(A,b);
time2=time();
x_SOR=SOR_ma(A,b,1.2);
time3=time();


time_jacobi=time1-time0;
time_gaussseidel=time2-time1;
time_SOR=time3-time2;

error_jacobi=np.linalg.norm(X-x_jacobi);
error_gaussseidel=np.linalg.norm(X-x_gaussseidel);
error_SOR=np.linalg.norm(X-x_SOR);

print('雅克比迭代时间为', time_jacobi);
print('误差为', error_jacobi);
print('高斯赛德尔迭代时间为', time_gaussseidel);
print('误差为', error_gaussseidel);
print('SOR迭代时间为', time_SOR);
print('误差为', error_SOR);


