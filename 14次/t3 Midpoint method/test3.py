
import matplotlib.pyplot as plt
import numpy as np
def pqt(p,q):
    temp=(p**2+q**2);
    return (-temp*q,temp*p)

def tixing(pi,qi,h):
    error=1e-14
    #为什么加大还崩了
    #不断迭代
    pi1=pi;qi1=qi;
    pi0=pi1+1;qi0=qi1+1;
    measure=1
    while(measure>error ):
    # for i in range(0,3):
        #存储
        pi0=pi1;qi0=qi1;
        #计算函数值
        pt,qt=pqt((pi+pi0)/2,(qi+qi0)/2)
        #迭代
        pi1=pi+h*pt;
        qi1=qi+h*qt;
        #一致收敛与我的区别
        measure=abs(pi1-pi0)+abs(qi1-qi0);
    return pi1,qi1

#中点公式
p=1;q=0

N=500000;
h=0.1;
x0=0;
x=[x0+h*i for i in range(0,N+1)];
p=np.zeros(N+1);
q=np.zeros(N+1)
p[0]=1;q[0]=0

for i in range(0,N):
    p[i+1],q[i+1]=tixing(p[i],q[i],h);
    # print(p[i+1])

plt.plot(p,q)

plt.xlabel('p',fontsize=20);
plt.ylabel('q',fontsize=20);
plt.title('Midpoint method',fontsize=20);
plt.tick_params(labelsize=20);

R=p**2+q**2;
maxR=max(R)
minR=min(R)
print("最大半径",maxR)
print("最小半径",minR)
print("半径误差",maxR-minR)