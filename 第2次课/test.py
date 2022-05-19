# 地址共享吗
import numpy as np
import math
def lang(numx,n):
    l=[];
    x=[0.32,0.34,0.36];
    # x0 = 0.32; x1 = 0.34; x2 = 0.36;
    y=[math.sin(0.32),math.sin(0.34),math.sin(0.36)];
    numy=0;
    # y0 = 0.314567; y1 = 0.333487; y2 = 0.352274;
    for i in range(0,n+1):
        num=1;
        for j in range(0,n+1):
            if(i!=j):
                num*=((numx-x[j])/(x[i]-x[j]));
        print(num)
        l.append(num);
    y=np.matrix(y[0:n+1]);#word，problem
    print(y)
    l=np.matrix(l);
    numy=np.sum(np.multiply(l,y));#function,这次都是行向量
    return numy

ry=math.sin(0.32);
fy=lang(0.32,1);
print("real",ry)
print("pre",fy)
print("err",fy-ry)



#目标是给定已知集合进行插值函数，给定等分或分等分定点集，
#计算插值。比较误差（最大值）