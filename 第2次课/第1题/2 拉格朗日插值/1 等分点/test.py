import numpy as np
import pandas as pd
import math 
from lagrangeinterpolation import lagrangeinterpolation
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
    # temp=1/(1+25*xi[i]**2)
    yi.append(temp);
#组合
xy=[xi,yi];#vstack作用
#创建分点
x1=[];
for i in range(0,num):#这里好像多了一个
    temp=a+(i/1000)*(b-a);
    x1.append(temp);#可以使用依次计算的方式，长度
#插值求点
y1=lagrangeinterpolation(xy,x1);#插值求点
#绘制推图像
np.squeeze(y1);
plt.plot(x1,y1);
#计算时间
time1=time.time();
#计算精确值与时间
# yexact=math.sin(math.pi*x1);#注意这里
# yexact=[1/(1+25*i**2) for i in x1 ]
# y1.tolist()
yexact=[math.sin(math.pi*i) for i in x1 ]
#接收
# yexact=np.asarray(yexact);#需要
#主要是any的问题
error=max(abs(y1-yexact));#有多个值
#输出
print("运算时间为",time1-time0);
print("误差为",error);
