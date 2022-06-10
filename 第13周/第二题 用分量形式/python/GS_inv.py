import numpy as np
def GS_ve(A,b):
    n=np.shape(A)[0]
    xk=np.matrix(np.ones((n,1)))
    xk1=np.matrix(np.zeros((n,1)))
    #每个x
    error=1e-10;
    xk=b.copy()
    for i in range(0,n):
        xk1[i,0]=(b[i,0]-A[i,0:i]*xk1[0:i,0]-A[i,i+1:n]*xk[i+1:n,0])/A[i,i]

    while(np.linalg.norm(xk-xk1)>error):
        xk=xk1.copy();
        for i in range(0,n):
            xk1[i,0]=(b[i,0]-A[i,0:i]*xk1[0:i,0]-A[i,i+1:n]*xk[i+1:n,0])/A[i,i]
    return xk1
