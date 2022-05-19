import numpy as np
def newtoninterpolation(x,y,x1 ):
    #计算下三角矩阵A
    n=len(x);
    m=len(x1);
    A= np.zeros((n,n));
    #pi0为1
    A[:,0]=1;
    #递推计算其他
    for i in range(1,n):
        #下三角，所以计算一半加对角
        #第0行有了就不计算了
        #使用首项和最后一项检验项数
        for j in range(1,i+1):
            A[i,j]=A[i,j-1]*(x[i]-x[j-1])
   
    #计算系数矩阵a
    a=np.zeros((n,1));
    a[0]=y[0];
    #转换为矩阵，注意数据维度
    for i in range(1,n):
        a[i,0]=(y[i]- sum(A[i,0:i]*a[0:i,0]) )/A[i,i];
    a=np.matrix(a)
    #计算待求点系数矩阵A
    A2= np.zeros((m,n));
    A2[:,0]=1;
    #递推计算其他
    for i in range(0,m):#从0开始
        #这里不是下三角,注意范围
        for j in range(1,n-1):
            A2[i,j]=A2[i,j-1]*(x1[i]-x[j-1])
    #计算待求点值
    y1=(A2*a).T;
    y1=y1.tolist();
    return y1[0];
