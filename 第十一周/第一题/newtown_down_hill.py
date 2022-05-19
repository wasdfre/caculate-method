
def f(x):
    return x**3-x-1;
    

def df(x):
    return 3*x**2-1;

def newtown_down_hill(left,right,x0):
    #初始值
    xi=x0;
    #误差限
    error=1e-14;
    #迭代公式
    x_temp=right;
    num_iter=0;
    while(abs(xi-x_temp)>error):
        x_temp=xi;
        #计算斜率
        yi=f(xi);
        # print(yi)
        dfx=df(xi);
        k=0;

        x_temp2=xi-(yi/dfx);
        while(abs(f(x_temp2))>abs(yi)):
            x_temp2=xi-(2**(-k))*(yi/dfx);
            k+=1;
            num_iter+=1;
            # print(k)
        xi=x_temp2;
        # print(xi)
    return xi,num_iter;

x,num_iter=newtown_down_hill(-5,5,0.5)

print("根为",x);
print("迭代次数为",num_iter);
print("误差为",f(x));

