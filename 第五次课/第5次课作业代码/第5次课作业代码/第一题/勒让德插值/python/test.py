from time import time
from legendregauss import legendregauss
from legendreinterpolationcoefficients import legendreinterpolationcoefficients
from legendreinterpolation import legendreinterpolation
from chebyshev import  chebyshevinterpolationcoefficients,chebyshevinterpolation
import numpy as np
from matplotlib import pyplot as plt
N=160;
#定义待插值函数
def u(x):
    return 1/(1+25*x**2);

M=1e6
#待求点
x1=np.array([-1+(2*i/M) for i in range(0,int(M+1))])

#真实值
yexact=[u(x1[i]) for i  in range(0,len(x1))]   

#这里的时间统计
time0=time();
#勒让德高斯罗巴托点
xi1=np.zeros(N+1)
xi1[1:-1]=legendregauss(N,1);
xi1[0]=-1;xi1[-1]=1;     
#对应y值
yi1=[u(xi1[i]) for i  in range(0,N+1)]
#勒让德插值系数
a=legendreinterpolationcoefficients(xi1,yi1);  
#勒让德插值系数
y1=legendreinterpolation(a,x1);  


time1=time();
#切比雪夫高斯罗巴托点
xi2=np.array([-np.cos(j*np.pi/N)  for j in range(0,N+1)])
#对应y值
yi2=[u(xi2[i]) for i  in range(0,N+1)]

#切比雪夫插值系数
a=chebyshevinterpolationcoefficients(xi2,yi2);   
        
#切比雪夫插值结果
y2=chebyshevinterpolation(a,x1) 


#时间
runtime2=time()-time1;
runtime1=time1-time0;      
#绘制图像
plt.subplot(2,1,1)
fig1 = plt.figure('勒让德')
plt.plot(x1,y1);

plt.subplot(2,1,2)
fig2 = plt.figure('切比雪夫')
plt.plot(x1,y1);


error1=max(abs(y1-yexact));
error2=max(abs(y2-yexact));
print("勒让德运行时间",runtime1);
print("切比雪夫运行时间",runtime2);
print("勒让德误差",error1);
print("切比雪夫误差",error2);

