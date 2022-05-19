from xml.etree.ElementInclude import XINCLUDE
import numpy as np
from torch import matrix_exp

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
            xright=x
            x=x-legendre(n,m,x)/legendre(n,m+1,x)
            number_newton+=1;
        z.append(x)
        a=x+h
        b=a+h
    print("牛顿法平均迭代次数",number_newton/k)
    return np.array(z)

#使用勒让德插值-高斯罗巴托点
#关键点在于系数以及多项式值
#多项式值使用之前那个文件计算
#系数分为0-n-1与第N个
#高斯积分上半部分，下半部分使用正交性
# from random import gauss
#定义原函数
#先分开再整合，还是先整合再分开
def u(x):
    return 1/(1+25*x**2);
#定义上半部分积分
def integration(n,k):
    pass
#定义正交值
def inpterpoltion(N,x):
    #获得高斯罗巴托点
    x0=legendregauss(N,1);#关于这里点的个数
    #求解系数矩阵
    uk=[]
    for k in range(0,N+1):#n-1个
        if k!=N:
            fro=(2*k+1)/(N*(N+1));
        else: 
            fro=1/(N+1);
        temp=0;
        for j in range(0,N+1):#n个
            temp+=u(x0[j])*legendre(k,0,x0[j])/(legendre(N,0,x0[j]))
        uk.append(fro*temp);
    #求解函数值
    y=np.zeros(len(x),N+1);
    for i in range(0,len(x)):
        for j in range(0,N+1):
            y[i,j]=legendre(j,0,x[i])
    uk=np.matrix(uk);
    return y*uk.T;
#牛顿法搜索











