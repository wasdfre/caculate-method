

import numpy as np
# 积分函数
def f(x):
    return x**3 - 2 *x**2 + 7*x - 5;

#积分公式
def Netown_Coates(a,b,y,N):
    coff=[
        [1/2,1/2],
        [1/6,2/3,1/6],
        [1/8,3/8,3/8,1/8],
        [7/90,16/45,2/15,16/45,7/90],
        [19/288,25/96,25/144,25/144,25/96,19/288],
        [41/840,9/35,9/280,34/105,9/280,9/35,41/840],
        [751/17280,3577/17280,1323/17280,2989/17280,2989/17280,1323/17280],
        [989/28350,5888/28350,-928/28350,10496/28350,-4540/28350,10496/28350,-928/28350,5888/28350,989/28350]
    ];
    coff_use=np.array(coff[N-1]);
    return (b-a)*sum(coff_use*y);

#积分阶数
N=2;
#总点数
M=100*N;
#需要划分的区间数
K=int(M/N);
#[-1,1]x
#少了range
x=np.array([-1+2*i/N for i in range(0,N+1)]);
#积分边界
a=1;b=3;
#区间边界点
#除法为什么int
dx=np.array([a+(b-a)*i/K for i in range(0,K+1)]);
#分区间使用积分
#b-a为固定值
res=0;
for i in range(0,K):
    #边界
    left=dx[i];right=dx[i+1];
    #求出该区间x
    #不要[]，注意是1
    x_temp=left+1/2*(right-left)*(x+1);
    #求出该区间y
    y_temp=f(x_temp);
    #代入求积分,并加和
    res+=Netown_Coates(left,right,y_temp,N);

error=abs(res-62/3);
print(error);
# import numpy as np
# # 积分函数
# def f(x):
#     return x**3 - 2 *x**2 + 7*x - 5;

# #积分公式
# def Netown_Coates(a,b,y,N):
#     coff=[
#         [1/2,1/2],
#         [1/6,2/3,1/6],
#         [1/8,3/8,3/8,1/8],
#         [7/90,16/45,2/15,16/45,7/90],
#         [19/288,25/96,25/144,25/144,25/96,19/288],
#         [41/840,9/35,9/280,34/105,9/280,9/35,41/840],
#         [751/17280,3577/17280,1323/17280,2989/17280,2989/17280,1323/17280],
#         [989/28350,5888/28350,-928/28350,10496/28350,-4540/28350,10496/28350,-928/28350,5888/28350,989/28350]
#     ];
#     coff_use=np.array(coff[N-1]);
#     return (b-a)*sum(coff_use*y);

# #积分阶数
# N=2;
# #总点数
# M=100*N;
# #需要划分的区间数
# K=int(M/N);
# #[-1,1]x
# #少了range
# x=np.array([-1+2*i/N for i in range(0,N+1)]);
# #积分边界
# a=1;b=3;
# #区间边界点
# res=0;
# left=a;right=b;
# x_temp=left+1/2*(right-left)*(x+1);

# #求出该区间y
# y_temp=f(x_temp);
# #代入求积分,并加和
# res+=Netown_Coates(left,right,y_temp,N);

# error=abs(res-62/3);
# print(error);