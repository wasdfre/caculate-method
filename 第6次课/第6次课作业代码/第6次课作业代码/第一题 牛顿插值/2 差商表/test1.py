#牛顿插值
from time import time
from matplotlib import pyplot as plt
import numpy as np
from newtoninterpolation import newtoninterpolation

def convert(a,b,xi):
    # x=1/2*((b-a)*xi+a+b);
    x=(a+(b-a)/2*(xi+1));
    return x;
def f(x):
    return 1/(1+x**2);
time0=time();
#分区间
a=-5;b=5;
K=4;
le=b-a;
interval=[a+le*i/K for i in range(0,K+1)];
#每个区间插值阶数
N=32;
#每个区间待求点个数
M=10*N;
#选择-1，1插值结点为切比雪夫罗巴托点
# t=[-1+np.cos(np.pi*i/N) for i in range(0,N+1)];
t=[np.cos(np.pi*i/N) for i in range(0,N+1)];
#计算每个区内插值结点
#存储最终结果
x_final=[];y_final=[]
#计算每个区内插值结点
for i in range(0,K):#这里是K吧
    #每个小区间左右边界
    left=interval[i];right=interval[i+1];
    #每个小区间对应插值点
    x=[];y=[];
    x=[convert(left,right,ti) for ti in t];
    y=[f(xi) for xi in x];
    #每个小区间对应待求点
    le_temp=right-left;
    x1=[left+le_temp*i/M for i in range(0,M+1)];
    #待求点求解
    y1=newtoninterpolation(x,y,x1);
    #保存每个区间结果
    x_final.extend(x1);
    y_final.extend(y1);

#比较结果
plt.plot(x_final,y_final);
runtime=time()-time0;

y_exact=[f(xi) for xi in x_final];
#这里
error=np.linalg.norm(np.array(y_final)-(np.array(y_exact)));
print("error",error);
print("runtime",runtime);