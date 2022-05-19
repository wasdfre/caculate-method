import numpy as np
#问题在于方法的选择
def f(x,a):
    return np.tan(x)-a*x;

#为什么这个形式
# def df(x):
#     return 2+1/(np.tan(x)**2)

def newtown_df(left,right,x0,a):
    if(not f(left,a) or not f(right,a)):
        return  left,0 if  not f(left,a)  else right
    #初始值
    xi=x0;
    #误差限
    error=1e-14;
    #迭代公式
    x_temp=right;
    y_temp=f(x_temp,a)
    number_iter=0;
    # print(xi,x_temp,y_temp)
    #斜率太大了
    #两种误差
    while(abs(f(xi,a))>error):
        #计算斜率
        yi=f(xi,a);
        df=(yi-y_temp)/(xi-x_temp);
        

        #存储
        x_temp=xi;
        y_temp=yi;

        #迭代
        xi=xi-yi/df;
        # print(2222,xi)
        number_iter+=1;
    # print(111,xi)
    return xi,number_iter;

#当系数为a时计算计算K个根\
K=3;
a=-1;
#小区间长度,但感觉pi不好算，换个整数？
# h=3;
h=np.pi;
#初始值
left=0;right=left+h/2;
number_iter=0
x=[];
#每个小区间使用
#不能跨两个区间
for i in range(0,K):
    #初始点取中点
    x0=(left+right)/2;
    xi,iter_temp=newtown_df(left,right,x0,a);
    # print(1111,left,right,x0);
    x.append(xi);
    number_iter+=iter_temp;
    i=i+1;
    ##更新边界  
    if(left==0):
        left=right;right=right+h/2;
    else:
        left=right;right=right+h;
    

print("零点为",x);
# print("误差为",error);
print("平均迭代次数为",number_iter/K)
#会出去的问题