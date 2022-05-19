
import numpy as np
# 积分函数
def f(x):
    return 1/(1+x**2);

#积分公式
def Netown_Coates(h,y):
    coff=np.array([7,32,12,32,14,7]);
    return h/90*sum(coff*y);

#积分阶数
N=4;
#总点数
M=100*N;
#需要划分的区间数
K=int(M/N);
#积分边界
a=-5;b=5;

#区间长度
h=(b-a)/K;
Y=[a,0,0,0,0,b]
res=0;
x_temp=a;
for i in range(0,K):
    #边界
    for j in range(1,5):
        x_temp+=1/4*h;
        Y[j]+=f(x_temp);

res+=Netown_Coates(h,Y);

error=abs(res-2*np.arctan(5));
print(error);

