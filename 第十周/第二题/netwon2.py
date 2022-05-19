
#计算函数值
def f(x):
    return x**3-x-1;

#计算一阶导数值
def df(x):
    return 3*x**2-1;


def netown(x0,h):
    #误差限
    number_iter=0;
    error=1e-14;
    #初始点
    xi=x0;
    #定义目的是限制误差
    x_temp=x0+h
    #迭代公式 
    while(abs(xi-x_temp)>error):
        x_temp=xi;
        # print(x_temp)
        xi=xi-f(xi)/df(xi);
        number_iter+=1;
        # print(1111,xi,f(n,m,xi))
    return (xi,number_iter);

#初始值
x0=0.5;
#限定区间长度
h=2
#误差
res,number_iter=netown(x0,h);

error=abs(f(res));
print("零点为",res);
print("误差为",error);
print("平均迭代次数为",number_iter)
#  x=[x(1)-double(f(x(1))/f1(x(1))),x]; 构造序列方法