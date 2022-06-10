
import matplotlib.pyplot as plt
import numpy as np
def pqt(p,q):
    temp=(p**2+q**2);
    return (-temp*q,temp*p)

#显式欧拉
#初值
p=1;q=0
#条件设定
N=4500;
h=0.01;
#x
#一个公共的隐藏变量
#x0=0;
#x=[x0+h*i for i in range(0,N+1)];
p=np.zeros(N+1);
q=np.zeros(N+1)
p[0]=1;q[0]=0
#解方程
for i in range(0,N):
    pt,qt=pqt(p[i],q[i])
    p[i+1]=p[i]+h*pt;
    q[i+1]=q[i]+h*qt;
plt.plot(p,q)

plt.xlabel('p',fontsize=20);
plt.ylabel('q',fontsize=20);
plt.title('Explicit Euler method',fontsize=20);
plt.tick_params(labelsize=20)
R=p**2+q**2;
maxR=max(R)
minR=min(R)
print("最大半径",maxR)
print("最小半径",minR)