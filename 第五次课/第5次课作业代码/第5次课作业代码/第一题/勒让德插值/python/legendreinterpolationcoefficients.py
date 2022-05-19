import numpy as np

def legendreinterpolationcoefficients( xi,yi ):

    N=len(xi)-1;
    #计算勒让德系数
    # 需要从0-N的Ln(xj)以及0-N-1的Lk(xj)
    L=np.zeros((N+1,N+1));
    for j in range(0,N+1):
        #这样会导致中间重复计算了很多次
        # L[k,j]=legendre(k,0,xi[j]);
        z=xi[j];
        #前两个的值
        k=0;L[k,j]=1
        k=1;L[k,j]=z;
        for k in range(1,N):
            L[1+k,j]=1/(k+1)*((2*k+1)*z*L[k,j]-k*L[k-1,j]);
    #计算N+1个插值系数

    a=np.zeros(N+1);
    #前N个
    for k in range(0,N):
        for j in range(0,N+1):
            a[k]=a[k]+yi[j]*L[k,j]/(L[N,j]**2);
        a[k]=a[k]*(2*k+1)/(N*(N+1));
    #第N+1个
    for j in range(0,N+1):
        a[N]=a[N]+yi[j]/L[N,j] 
    a[N]=a[N]/(N+1);
    return a;
    