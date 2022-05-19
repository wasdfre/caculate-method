import numpy as np
import pandas as pd
import math 
from polynomialinterpolation import polynomialinterpolation
import matplotlib.pyplot as plt
import time
# import polynomialinterpolation
#给定范围，给定定点集，待求集个数
time0=time.time();
a=-1;b=1;
N=10;
num=1000;
# N=100;

#创建定点x(1000个)

xi=[];
for i in range(0,N+1):#0,N
    temp=a+(i/N)*(b-a);
    xi.append(temp);#可以使用依次计算的方式
#创建定点y
yi=[];
for i in range(0,N+1):
    temp=math.sin(math.pi*xi[i]);
    yi.append(temp);
#组合
xy=[xi,yi];#vstack作用
#创建分点
x1=[];
for i in range(0,num):#这里好像多了一个
    temp=a+(i/1000)*(b-a);
    x1.append(temp);#可以使用依次计算的方式，长度
#插值求点
y1=polynomialinterpolation(xy,x1);#插值求点
np.squeeze(y1);
#绘制推图像
plt.plot(x1,y1);
#计算时间
time1=time.time();
#计算精确值与时间
# yexact=math.sin(math.pi*x1);#注意这里
yexact=[math.sin(math.pi*i) for i in x1 ]
error=max(abs(y1-yexact));
#输出
print("运算时间为",time1-time0);
print("误差为",error);
