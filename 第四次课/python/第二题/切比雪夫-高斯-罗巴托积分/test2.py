# -*- coding: utf-8 -*-
from tkinter import W
import numpy as np
from torch import zero_

def legendre(n,m,x):
    if n==0:
        if m>=1:
            return 0
        else:
            return 1
    
    
    s=np.zeros([n+1,m+1])
    
    for j in range(0,m+1):
       if j==0:
          s[0,j]=1
          s[1,j]=x
          for k in range(1,n):
            s[k+1,j]=((2*k+1)*x*s[k,j]-k*s[k-1,j])/(k+1)
          
       else:
           s[0,j]=0
           if j==1:
               s[1,j]=1
           else:
               s[1,j]=0
           
           for k in range(1,n):
               s[k+1,j]=(2*k+1)*s[k,j-1]+s[k-1,j]
           
    r=s[n,m]
    
    return r





def legendregauss(n,m):
    if n==0:
        return []

    z=[]
    error=1e-14
    h=n**(-2)
    a=-1
    b=a+h
    
    for k in range(1,n-m+1):
    
        legendre_a=legendre(n,m,a)
        legendre_b=legendre(n,m,b)
        while(legendre_a*legendre_b>0):
            a=b
            legendre_a=legendre_b
            
            b=a+h
            legendre_b=legendre(n,m,b)
    
        x=(a+b)*0.5
        xright=b
        while(np.abs(x-xright)>error):
            xright=x
            x=x-legendre(n,m,x)/legendre(n,m+1,x)
    
        z.append(x)
        a=x+h
        b=a+h
    
    return np.array(z)



def f(x):
    return 1/(1+25*x**2)


N=80
#高斯点%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#求零点
x=legendregauss(N+1,0);
#求y值
y=[f(x[j]) for j in range(0,N+1)];
y=np.array(y);
#求w
w=np.zeros(N+1)
for k in range(0,N+1):
    w[k]=2/((1-x[k]**2)*(legendre(N+1,1,x[k]))**2);
#求积分


I=np.sum(y*w);
error_le_gauss=abs(I-2/5*np.arctan(5));



#高斯洛巴托%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x_lobatto=np.zeros(N+1)
x_lobatto[0]=-1
x_lobatto[1:-1]=legendregauss(N,1)
x_lobatto[-1]=1
w_lobatto=np.zeros(N+1)
# for k in range(0,N):
for k in range(0,N+1)
    w_lobatto[k]=2/N/(N+1)/(legendre(N,0,x_lobatto[k]))**2;           #勒让德高斯罗巴托权重系数
# w_lobatto[N]=2/(N+1)/(legendre(N,0,x_lobatto[k]));
y_lobatto=np.zeros(N+1)
for k in range(0,N+1):
    y_lobatto[k]=f(x_lobatto[k])

I_lobatto=np.sum(y_lobatto*w_lobatto)           #勒让德-高斯-罗巴托 积分
error_le_gauss_lobatto=abs(I_lobatto-2/5*np.arctan(5))




N=int(1e2)
#切比雪夫高斯################################
x_gauss=np.array([-np.cos((2*j+1)*np.pi/(2*N+2))  for j in range(0,N+1)])           #切比雪夫高斯点
y_gauss=1/(1+25*x_gauss**2)*np.sqrt(1-x_gauss**2)
I_gauss=sum(y_gauss)*np.pi/(N+1)                                   #计算切比雪夫高斯积分
error_gauss=np.abs(I_gauss-2/5*np.arctan(5))

#切比雪夫高斯罗巴托################################
x_gauss_lobatto=np.array([-np.cos(j*np.pi/N)  for j in range(0,N+1)])           #切比雪夫高斯罗巴托点
y_gauss_lobatto=1/(1+25*x_gauss_lobatto**2)*np.sqrt(1-x_gauss_lobatto**2)          #1/(1+25*x**2)是被积函数
I_gauss_lobatto=(sum(y_gauss_lobatto)-y_gauss_lobatto[0]/2-y_gauss_lobatto[N]/2)*np.pi/N           #计算切比雪夫罗巴托高斯积分
error_gauss_lobatto=np.abs(I_gauss_lobatto-2/5*np.arctan(5))



#梯形积分求解################################
x_1_3=np.array([-1+2/N*j  for j in range(0,N+1)])           #[-1,1]等分点
y_1_3=1/(1+25*x_1_3**2)
I_1_3=(sum(y_1_3)-y_1_3[0]/2-y_1_3[-1]/2)*2/N               #公式(1.3)
error_1_3=np.abs(I_1_3-2/5*np.arctan(5))

print("勒让德高斯误差为:",error_le_gauss)
print("勒让德高斯洛巴托误差为:",error_le_gauss_lobatto)
print('切比雪夫高斯点误差为',error_gauss)
print('切比雪夫高斯洛巴托点误差为',error_gauss_lobatto)
print('equation (1.3)梯形积分',error_1_3)
# %梯形公式计算积分
# I_1_3=1/N*(x_1_3*y_1_3'-1/2(y_1_3(1)+y_1_3(end))