import numpy as np
def legendreinterpolation(a,x):
    N=len(a)-1;#插值系数
    M=len(x);#待求点

    y=np.zeros(M);#待预测y值
    for i in range(0,M):
        L=np.zeros(N+1);#定义为列向量
        z=x[i];
        #仍然需要从0-N的Pk(x)
        k=0;L[k]=1;
        k=1;L[k]=z;
        for k in range(1,N):
            L[1+k]=1/(k+1)*((2*k+1)*z*L[k]-k*L[k-1]);
        # if i<2:
        #     print(L)
        #     print(a)
        #     print(np.sum(np.multiply(L,a)))
        y[i]=np.sum(np.multiply(L,a));
    return y;
    