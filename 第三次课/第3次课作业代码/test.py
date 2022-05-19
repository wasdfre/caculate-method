from legendre import legendre
from matplotlib import pyplot as py
import pandas as pd
import numpy as np
n=20;#多项式阶数
m=8;#导数次数

#构造-1，1区间点
x=[-1];
while(x[-1]<=1):
    x.append(x[-1]+0.01);
y=[];
# y=pd.zeros(201)
# y0=(pd.toarray(y)*0).tolist();
# y=y0;#这里会指向同一个地址吗？
for k in range(0,201):
    y.append(legendre(n,m,x[k]));
y0=(np.array(y)*0).tolist();
py.subplot(1,2,1);
# py.hold(True);
# py.ylim(1.1*min(y),2*abs(min(y))
# py.yticks(1.1*min(y),2*abs(min(y)));
py.plot(x,y);
py.plot(x,y0);
# plt.show()
py.subplot(1,2,2);
# py.hold(True);
py.plot(x,y);#这个是干啥
py.plot(x,y0);
py.ylim(1.1*min(y),2*abs(min(y)))#对最近图修改
py.show()