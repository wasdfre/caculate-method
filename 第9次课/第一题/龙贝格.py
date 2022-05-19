
import numpy as np
# 积分函数
def f(x):
    return x**3 - 2 *x**2 + 7*x - 5;

#积分公式
def romberg_Coates(a,b,y):
    #龙贝格系数
    coff=np.array([0.038271604938272,
        0.180599647266314,
        0.062081128747795,
        0.180599647266314,
        0.076895943562610,
        0.180599647266314,
        0.062081128747795,
        0.180599647266314,
        0.038271604938272]);

    return (b-a)*sum(coff*y);

#积分阶数
N=8;
#总点数
M=100*N;
#需要划分的区间数
K=int(M/N);
x=np.array([-1+2*i/N for i in range(0,N+1)]);
#积分边界
a=1;b=3;
res=0;

dx=np.array([a+(b-a)*i/K for i in range(0,K+1)]);

for i in range(0,K):
    #边界
    left=dx[i];right=dx[i+1];
    #求出该区间x
    #不要[]，注意是1
    x_temp=left+1/2*(right-left)*(x+1);
    #求出该区间y
    y_temp=f(x_temp);
    #代入求积分,并加和
    res+=romberg_Coates(left,right,y_temp);

error=abs(res-62/3);
print(error);

# import numpy as np
# # 积分函数
# def f(x):
#     return x**3 - 2 *x**2 + 7*x - 5;

# #积分公式
# def romberg_Coates(a,b,y):
#     #龙贝格系数
#     coff=np.array([0.038271604938272,
#         0.180599647266314,
#         0.062081128747795,
#         0.180599647266314,
#         0.076895943562610,
#         0.180599647266314,
#         0.062081128747795,
#         0.180599647266314,
#         0.038271604938272]);

#     return (b-a)*sum(coff*y);

# #积分阶数
# N=8;
# x=np.array([-1+2*i/N for i in range(0,N+1)]);
# #积分边界
# a=1;b=3;
# res=0;

# left=a;
# right=b;
# #求出该区间x
# x_temp=left+1/2*(right-left)*(x+1);
# #求出该区间y
# y_temp=f(x_temp);
# #代入求积分,并加和
# res+=romberg_Coates(left,right,y_temp);

# error=abs(res-62/3);
# print(error);