# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:31:15 2020

@author: pc
"""
import numpy as np

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

x_lobatto=np.zeros(N+1)

x_lobatto[0]=-1
x_lobatto[1:-1]=legendregauss(N,1)
x_lobatto[-1]=1
#[-1,1]上勒让德高斯罗巴托点


w_lobatto=np.zeros(N+1)
for k in range(0,N+1):
   w_lobatto[k]=2/N/(N+1)/(legendre(N,0,x_lobatto[k]))**2;           #勒让德高斯罗巴托权重系数

y_lobatto=np.zeros(N+1)
for k in range(0,N+1):
    y_lobatto[k]=f(x_lobatto[k])

I_lobatto=np.sum(y_lobatto*w_lobatto)           #勒让德-高斯-罗巴托 积分
error_gauss_lobatto=abs(I_lobatto-2/5*np.arctan(5))

print("勒让德高斯洛巴托误差为:",error_gauss_lobatto)





