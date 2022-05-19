import numpy as np
def newtoninterpolation(x,y,x1 ):
    #计算下三角矩阵A
    n=len(x);
    m=len(x1);
    A= np.zeros((n,n));
    A[:,0]=y;
    #就是拿左边两个计算右边一个，为什么倒着构造
    # a=np.zeros((n,1));
    #从左往右，从上往下
    # for i in range(1,n):
    #     for j in range(1,i):
    #         A[i,j]=(A[i,j-1]-A[i-1,j-1])/(x[i]-x[i-j])
    #     #获取最后一个
    #     a[i,0]=A[i,j];
    #另一种
    for j in range(1,n):
        for i in range(0,n-j):
            A[i,j]=(A[i,j-1]-A[i+1,j-1])/(x[i]-x[i+j])
    a=A[0,:]
    a=np.matrix(a).T
    #计算待求点系数矩阵A
    A2= np.zeros((m,n));
    A2[:,0]=1;
    #递推计算其他
    for i in range(0,m):
        #这里不是下三角,注意范围
        for j in range(1,n-1):
            A2[i,j]=A2[i,j-1]*(x1[i]-x[j-1])

    #计算待求点值

    y1=(np.matrix(A2)*a).T;
    y1=y1.tolist();
    return y1[0];
