
import numpy as np
#计算n阶勒让德，m阶导数的值

def legendre(n,m,x):
    if n==0:
        if m>=1:
            return 0
        else:
            return 1
    s=np.zeros([n+1,m+1])
    
    for j in range(0,m+1):
       if j==0:
          s[0,j]=1
          s[1,j]=x
          for k in range(1,n):
            s[k+1,j]=((2*k+1)*x*s[k,j]-k*s[k-1,j])/(k+1)
          
       else:
           s[0,j]=0
            
            
           if j==1:
               s[1,j]=1
           else:
               s[1,j]=0
           
           for k in range(1,n):
               s[k+1,j]=(2*k+1)*s[k,j-1]+s[k-1,j]        
    r=s[n,m] 
    return r;

#计算函数值
def f(n,m,x):
    return legendre(n,m,x);

#计算一阶导数值
def df(n,m,x):
    return legendre(n,m+1,x);

#勒让德函数一个区间——牛顿法求零点
def netown(n,m,x0,h):

    number_iter=0;
    #误差限
    error=1e-14;
    #初始点
    xi=x0;
    #定义目的是限制误差
    x_temp=x0+h
    #迭代公式 
    print()
    while(abs(xi-x_temp)>error):
        x_temp=xi;
        # print(x_temp)
        xi=xi-f(n,m,xi)/df(n,m,xi);
        number_iter+=1;
        # print(1111,xi,f(n,m,xi))
    return (xi,number_iter);


#勒让德函数——牛顿法求零点
def legendre_netown(n,m):
    #每个零点间距
    h=n**(-2);
    #区间边界
    left=-1;right=left+h;
    #存储零点
    x=[];
    #统计零点个数
    i=0;
    #
    number_iter=0;
    #总共n-m+1个点
    for k in range(1,n-m+1):
    # while(left<1):
        #更新边界   
        f_left=legendre(n,m,left);
        f_right=legendre(n,m,right);
        while(f_left*f_right>0):
            left=right;right=left+h;
            f_left=f_right;
            f_right=legendre(n,m,right)
       
        #每个小区间使用牛顿法找零点
        #初始点取中点
        x0=(left+right)/2;
        xi,iter_temp=netown(n,m,x0,h);
        # print(222,xi)
        x.append(xi);
        number_iter+=iter_temp;
        i=i+1;
        #更新
        left=xi+h;right=left+h;
        # print(left)
        
    return x,number_iter/n-m+1;
#阶数

n=8;
m=1;
res,number_iter=legendre_netown(n,m);
# error=np.linalg.norm(res);
print("零点为",res);
# print("误差为",error);
print("平均迭代次数为",number_iter)

#有n-1个零点,已知数量使用for
#while记得设置次数限制
#多级导数还是直接作为参数吧
#边界条件
# #更新边界   
# f_left=legendre(n,m,left);
# f_right=legendre(n,m,right);
# while(f_left*f_right>0):
#     left=right;right=left+h;
#     f_left=f_right;
#     f_right=legendre(n,m,right)
#x——temp是x的上一个值
#  left=right;right=left+h; 最后更新
#left=x+h;right=left+h;注意
