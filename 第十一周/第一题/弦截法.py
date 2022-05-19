
def f(x):
    return x**3-x-1;

# def df(x):
#     return 3*x**2-1;

def newtown_df(left,right,x0):
    #初始值
    xi=x0;
    #误差限
    error=1e-14;
    #迭代公式
    x_temp=right;
    y_temp=f(x_temp);
    num_iter=0;
    while(abs(xi-x_temp)>error):
        #计算斜率
        yi=f(xi);
        df=(yi-y_temp)/(xi-x_temp);

        #存储
        x_temp=xi;
        y_temp=yi;

        #迭代
        xi=xi-yi/df;
        num_iter+=1;
    return xi,num_iter;

x,num_iter=newtown_df(-5,5,0.5)

print("根为",x);
print("迭代次数为",num_iter);
print("误差为",f(x));