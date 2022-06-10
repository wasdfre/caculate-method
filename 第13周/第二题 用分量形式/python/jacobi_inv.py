import numpy as np
def J_ve(A,b):
    n=np.shape(A)[0]
    xk=np.matrix(np.ones((n,1)))
    xk1=np.matrix(np.zeros((n,1)))
    error=1e-10
    xk=b.copy()
    for i in range(0,n):
        xk1[i,0]=(b[i,0]-A[i,:]*xk[:,0])/A[i,i]+xk[i,0]
    # print(np.linalg.norm(xk-xk1))
    #这怎么标准不统一
    while(np.linalg.norm(xk-xk1)>error):
        xk=xk1.copy();
        for i in range(0,n):
            xk1[i,0]=(b[i,0]-A[i,:]*xk[:,0])/A[i,i]+xk[i,0]
    return xk1