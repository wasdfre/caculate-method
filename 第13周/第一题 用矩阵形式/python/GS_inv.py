import numpy as np

def decompose(A):
    L=-np.tril(A,-1)
    U=-np.triu(A,1)
    D=np.diag(np.diag(A,0));
    return L,U,D

def GS_ma(A,b):
    #分解
    L,U,D=decompose(A)
    DLinv=np.linalg.inv(D-L)
    #B
    B=np.dot(DLinv,U)
    #g
    g=np.dot(DLinv,b)
    #初值
    # n=np.shape(A)[0]
    xk=g.copy();
    xk1=np.dot(B,xk)+g;
    #迭代,条件
    error=1e-14
    while(np.linalg.norm(xk-xk1)>error):
        xk=xk1.copy()
        xk1=np.dot(B,xk)+g
    return xk1