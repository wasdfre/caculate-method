import numpy as np

def decompose(A):
    L=-np.tril(A,-1)
    U=-np.triu(A,1)
    D=np.diag(np.diag(A,0));
    return L,U,D

def SOR_ma(A,b,w):
    #分解
    L,U,D=decompose(A)
    DWLinv=np.linalg.inv(D-w*L)
    #B
    B=np.dot(DWLinv,((1-w)*D+w*U))
    #g
    g=np.dot(DWLinv,(w*b))
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