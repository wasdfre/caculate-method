import numpy as np

def downtri(A,Y):
    m=A.shape[0]
    x=np.zeros(m)
    for k in range(0,m):
        x[k]=(Y[k]-np.dot(A[k,0:k],x[0:k]))/A[k,k]
        # print(k,Y[k],A[k,0:k],x[0:k],A[k,k])
    return x

def uptri(A,Y):
    m=A.shape[0]
    x=np.zeros(m)
    for k in range(0,m):
        x[m-k-1]=(Y[m-k-1]-np.dot(A[m-k-1,m-k:m],x[m-k:m]))/A[m-k-1,m-k-1]
        # print(k, x[m-k-1],Y[m-k-1],A[m-1,m-k:m],x[m-k:m],A[m-k-1,m-k-1])
    return x

def LUP(A):
    #计算各种L
    #尺寸
    N=A.shape[0];
    #循环n-1
    L=[];
    P=np.eye(N);
    for k in range(0,N-1):
        #注意最后一个
        #创建P
        pk=np.eye(N);
        idx=np.argmax(abs(A[k,k:N]))
        pk[:,[k,k+idx]]=pk[:,[k+idx,k]];
        P=np.dot(P,pk)
        #右乘
        A=np.dot(A,pk)
        lk=np.eye(N);
        for i in range(k+1,N):   
            #填充元素
            lk[i,k]=-A[i,k]/A[k,k];
        #保存
        L.append(lk);
        # print(lk)
        #左乘作用;
        A=np.dot(lk,A);

    #计算L
    L1=np.matrix(N*np.eye(N)-sum(L));
    # print(L1)
    U=np.matrix(A);
    
    return L1,U,P;

def LU(A,N):
    L=np.zeros((N,N));
    U=np.zeros((N,N));
    for k in range(0,N):
        L[k,k]=1
        #先算u
        for j in range(k,N):
            if(k==0):
                U[k,j]=A[k,j];
                
            else:
                U[k,j]=A[k,j]-np.dot(L[k,0:k],U[0:k,j]);
        #再算l
        for i in range(k+1,N):
            if(k==0):
                L[i,k]=A[i,k]/U[k,k];
            else:
                L[i,k]=((A[i,k]-np.dot(L[i,0:k],U[0:k,k]))/U[k,k]);
    return L,U


#求解常数边值问题 c1*p(x)u''+q(x)u'+c2*u=F(x),ua=,ub=
#求解微分矩阵
#含有k的边界需要注意，保证mat与python一致
def D_matrix(N):
    d=np.zeros((N+1,N+1))
    x=[np.cos(np.pi*i/N) for i in range(0,N+1)]
    c=np.ones(N+1)
    c[0]=2;c[-1]=2;
    for k in range(0,N+1):
        for j in range(0,N+1-k):
            if(j==0 and k==0):
                d[j,k]=(2*N**2+1)/6;
            elif(j==N and k==N):
                d[j,k]=-d[1,1];
            elif(j==k):
                d[j,k]=-x[k]/(2*(1-x[k]**2));
            else:
                d[j,k]=c[j]*(-1)**(j+k)/(c[k]*(x[j]-x[k])); 
           
    for k in range(1,N+1):
        for j in range(N+1-k,N+1):
            d[k,j]=-d[N-k,N-j]; 
            # print((j,k),d[j,k])
    return d;

#p(x)
def p(x):
    return x;

def q(x):
    return -1;

def f(x):
    return (24+5*x)*np.exp(5*x)+(2+2*x**2)*np.cos(x**2)-(1+4*x**2)*np.sin(x**2);

def y(x):
    return np.exp(5*x)+np.sin(x**2);
#构造插值点
N=128;
#按照中间点，边界点的分界更符合逻辑
X=np.zeros(N+1);
for i in range(0,N+1):
    X[i]=np.cos(np.pi*i/N);
Y=y(X);

#求解原始矩阵 D1,D2,P,Q,F
F=np.zeros((N+1,1));
#对角阵（点对点相乘)
P=np.zeros((N+1,N+1));
Q=np.zeros((N+1,N+1));
for k in range(0,N+1):#全体参与运算
    F[k,0]=f(X[k]);
    P[k,k]=p(X[k]);
    Q[k,k]=q(X[k]); 

D1=D_matrix(N);
#注意含义
D2=np.dot(D1,D1);

#构造矩阵AU=F'(1,n-1)
A=np.zeros((N+1,N+1));
A=D2+np.dot(P,D1)+Q;
#直接赋值有拷贝问题，矩阵运算不会
Y1=np.zeros((N+1,1));
Y1[0]=Y[0];Y1[-1]=Y[-1];

F0=np.zeros((N-1,1));
F0[0:N-1,0]=F[1:N,0];
#关于其他
A0=np.zeros((N-1,N-1));
#关于初值
A1=np.zeros((N-1,N+1));

A0[0:N-1,0:N-1]=A[1:N,1:N];
A1[0:N-1,0:N+1]=A[1:N,0:N+1];

F1=np.dot(A1,Y1);

#一般方法
#U1=np.dot(np.linalg.pinv(A0),(F0-F1));
#print("error",np.linalg.norm(U1-Y[1:N]));

#直接LU分解求
l1,u1=LU(A0,N-1);
y1=downtri(l1,(F0-F1));
U2=uptri(u1,y1);

# LUP分解求
l2,u2,p2=LUP(A0);
# print(l2)
y2=downtri(l2,(F0-F1));
y3=uptri(u2,y2);
U3=np.dot(p2,y3)
#不对应，大概率顺序问题
errorLU=np.linalg.norm(U2-Y[1:N]);
errorLUP=np.linalg.norm(U3-Y[1:N]);
print("errorLU",errorLU);
print("errorLUP",errorLUP);
#不可以按照傅里叶分解的方式解吗？