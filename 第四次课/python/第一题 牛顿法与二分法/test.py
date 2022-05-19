from legendregauss_bisection import legendregauss_bisection
from time import time
from Newtown import legendregauss
from legendre import legendre
# from matplotlib import pyplot as py
import pandas as pd
import numpy as np

#format报错，如何指定全局数据类型
N=10;#多项式阶数
m=0;#导数次数

#二分法求零点时间
time1=time();
x_bisection=legendregauss_bisection(N,m); 
time2=time();
time_bisection=time2-time1;
#print(x_bisection)
#牛顿法求零点时间
x_Newton=legendregauss(N,m);
time3=time();
time_Newton=time3-time2;

#二分法误差
error_bisection=0;
for k in range(0,N-m):
    error_bisection=abs(legendre(N,m,x_bisection[k]))+error_bisection;
error_bisection=error_bisection/(k+1)

#牛顿法误差
error_Newton=0;
for k in range(0,N-m):
    error_Newton=abs(legendre(N,m,x_Newton[k]))+error_Newton;
error_Newton=error_Newton/(k+1)

print("二分法速度",time_bisection)
print("牛顿法速度",time_Newton)
print("二分法误差",error_bisection)
print("牛顿法误差",error_Newton)