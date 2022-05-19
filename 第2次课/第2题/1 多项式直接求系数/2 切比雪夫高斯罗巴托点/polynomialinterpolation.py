import numpy as np
import pandas as pd
# import math 
# import matplotlib.pyplot as plt
# import time
def polynomialinterpolation(xy,x):
    #获取定点集
    n=len(xy[0]);
    #获取定点集x,y
    # x0=(np.array(xy[0])).T;#转置的目的
    x0=xy[0];
    y0=xy[1];

    #待求集长度
    m=len(x);
    
    #设定X
    X=np.zeros((n,n))#这次的n是总数个
    #计算A
    for i in range(0,n):
        temp=x0[i];
        X[i,0]=1;#选取方式差别
        for j in range(1,n):
            X[i,j]=X[i,j-1]*temp;

    #计算待求y
    y0=np.matrix(y0).T
    a=np.linalg.inv(X)*y0 #矩阵。I，pinv与inv
    y=[]
    for i in range(0,m):
        temp=x[i];
        M=np.zeros((1,n))
        M[0]=1;#选取方式差别
        for j in range(1,n):
            M[0,j]=M[0,j-1]*temp;#两种数据类型的取值
        temp1=M.dot(a)
        # np.squeeze(temp1)
        # print(temp1)
        y.append(temp1);
    y=np.asarray(y);#需要
    y=np.squeeze(y)#需要接收
    return y#注意none