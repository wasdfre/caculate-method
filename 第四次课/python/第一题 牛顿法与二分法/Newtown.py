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
    number_newton=0;
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
            x=x-legendre(n,m,x)/legendre(n,m+1,x)
            number_newton+=1;
        z.append(x)
        a=x+h
        b=a+h
    print("牛顿法平均迭代次数",number_newton/k)
    return np.array(z)














