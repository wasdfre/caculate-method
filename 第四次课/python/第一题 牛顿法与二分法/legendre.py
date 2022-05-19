
import numpy as np
def legendre(n,m,x):
    #n为多项式项，m为导数次数
    #动态规划
    s=np.zeros((n+1,m+1),dtype=float);
    for j in range(0,m+1):#m次
        #先求n阶多项式值
        if(j==0):                   #如果j为0，即不求导数下
            s[0,j]=1;s[1,j]=x;      #0,1
            for k in range(1,n):  #注意范围
                #公式1
                s[k+1,j]=((2*k+1)*x*s[k,j]-k*s[k-1,j])/(k+1);
        else: 
        #再求高阶
            s[0,j]=0                #0阶
            if j==1:                #1阶
                s[1,j]=1;
            else:
                s[1,j]=0;
            for k in range(1,n):    #其他阶次，高阶导数同样遵循
                s[k+1,j]=(2*k+1)*s[k,j-1]+s[k-1,j];
    return s[n,m];
