import matplotlib.pyplot as plt
import numpy as np
def pqt(pq):
    p=pq[0];
    q=pq[1]
    temp=(p**2+q**2);
    return np.array([-temp*q,temp*p])
#龙格库塔

def runge_kutta(pi,qi,h):
    #对于x和y的认识
    #array与[]运算限制
    pq=np.array([pi,qi])
    k1=pqt(pq);
    k2=pqt(pq+h/2*k1);
    k3=pqt(pq+h/2*k2);
    k4=pqt(pq+h*k3);
    
    pqi=pq+h/6*(k1+2*k2+2*k3+k4)
    return pqi[0],pqi[1]


#龙格库塔
p=1;q=0

N=500000;
h=0.1;
x0=0;
x=[x0+h*i for i in range(0,N+1)];
p=np.zeros(N+1);
q=np.zeros(N+1)
p[0]=1;q[0]=0

for i in range(0,N):
    p[i+1],q[i+1]=runge_kutta(p[i],q[i],h);
    # print(p[i+1])

plt.plot(p,q)

plt.xlabel('p',fontsize=20);
plt.ylabel('q',fontsize=20);
plt.title('Runge-Kutta method',fontsize=20);
plt.tick_params(labelsize=20)
R=p**2+q**2;
maxR=max(R)
minR=min(R)
print("最大半径",maxR)
print("最小半径",minR)
print("半径误差",maxR-minR)
