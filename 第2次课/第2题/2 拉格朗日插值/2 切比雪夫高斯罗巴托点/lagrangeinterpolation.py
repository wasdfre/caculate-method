
import numpy as np
# import pandas as pd
def lagrangeinterpolation(xy,x):
    n=len(xy[0]);

    #获取定点集x,y
    x0=xy[0];
    y0=xy[1];
    #待求集长度
    m=len(x);
    #求l[]
    l=np.zeros((m,n));
    for i in range(0,m):
        #指定x，指定k，计算l
        tempx=x[i];
        for k in range(0,n):
            templ=1;
            for j in range(0,n):
                if(j!=k):
                    templ*=((tempx-x0[j])/(x0[k]-x0[j]));#这里是x0
            l[i,k]=templ;

    y0=np.matrix(y0);#word，problem
    # l=np.matrix(l);
    # x=np.matrix(x);
    y=l*y0.T;#function 这次都是行向量,最后结果是矩阵，mulsum出错
    y=np.asarray(y);#需要
    y=np.squeeze(y)#需要接收
    return y