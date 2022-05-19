import numpy as np

def f(x,a):
    return np.tan(x)-a*x;

#为什么这个形式
def df(x,a):
    return 1+a+(np.tan(x)**2)

def two_divide(left,right,a):
    if(not f(left,a) or not f(right,a)):
        return  left if  not f(left,a)  else right
    error=0.1;
    mid=(left+right)/2;
    while(f(mid,a)>error):
        mid=(left+right)/2;
        if(f(left,a)*f(mid,a)<0):
            right=mid;
        else:
            left=mid;
        # print(mid);
    
    return (right+left)/2;

def newtown_down_hill(left,right,a):
    if(not f(left,a) or not f(right,a)):
        return  left if  not f(left,a)  else right
    #初始值
    xi=two_divide(left,right,a);
    #误差限
    error=1e-14;
    #迭代公式
    x_temp=right;
    #注意绝对值
    while(abs(f(xi,a))>error and abs(xi-x_temp)>error):
        x_temp=xi;
        #计算斜率
        yi=f(xi,a);
        # print(yi)
        dfx=df(xi,a);
        k=0;

        x_temp2=xi-(yi/dfx);
        #限制在一个区间内
        while(abs(f(x_temp2,a))>abs(yi) or x_temp2<left or x_temp>right):
            x_temp2=xi-(2**(-k))*(yi/dfx);
            k+=1;
            # print(k)
        xi=x_temp2;
        # print(1111,xi,yi)
    return xi;

#当系数为a时计算计算K个根\
K=1000;
a=-1;
#小区间长度,但感觉pi不好算，换个整数？
# h=3;
h=np.pi;
#初始值
left=0;right=left+h/2;
x=[];
#每个小区间使用
#不能跨两个区间
for i in range(0,K):
    xi=newtown_down_hill(left,right,a);
    # print(1111,left,right,x0,xi);
    x.append(xi);
    # number_iter+=iter_temp;
    i=i+1;
    ##更新边界  
    #边界的参数，左开右闭
    right=right+h; left=right-h+1e-14;  
    # print(2222,left,right);

print("零点为",x);