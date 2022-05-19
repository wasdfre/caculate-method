#用二分法计算Pn+1(x)与Pn'(x)=0
#首先需要计算Pn+1
#主要是划分区间
#计算勒让德的方式
from legendre import legendre#
import math as ma
def bisection(n,m,alpha,beta,error):
    #异常检测
    if alpha<beta:
        a=alpha;
        b=beta;
    else:
        b=alpha;
        a=beta;
    #直接计算次数，向上取整(区间长度误差)
    
    N=ma.ceil(ma.log2((b-a)/error))
    #如果函数值满足条件直接返回,虽然这个误差表征区间长度
    if (abs(legendre(n,m,a))<error or abs(legendre(n,m,b))<error):
        x=(a+b)/2;#蹭一步精度
        return x,N;#注意返回方式

    
    for i in range(1,N+1):
       
        mid=(a+b)/2;
        legendre_mid=legendre(n,m,mid);
        legendre_a=legendre(n,m,a);
        if(legendre_a*legendre_mid<0):
            b=mid;
        else:
            a=mid
         #即使加入了函数值检测，也应该是先判区间，然后判精度
        if (abs(legendre_mid)<error):
            x=(a+b)/2;
            return  x,N;
    x=(a+b)/2;
    return  x,N;


#二分法求解n阶m次导数下勒让德高斯点
def legendregauss_bisection(n,m):
    #异常检测a
    z=[];
    if(n==0 or m>=n):
        return z;
    #误差限
    error=1e-18;
    #最小间隔
    h=n**(-2);
    #初始边界
    a=-1;b=a+h;
    #分割
    number_bisection=0;
    #共有n-m个互异零点
    for k in range(0,n-m):
        #迭代区间寻找零点位置，即分割出只有一个0点的区间
        legendre_a=legendre(n,m,a);
        legendre_b=legendre(n,m,b);
        while(legendre_a*legendre_b>0):
            a=b;
            legendre_a=legendre_b;
            
            b=a+h;
            legendre_b=legendre(n,m,b);
            # print(b,"bbb")
        #在一个零点区间调用二分法
        temp,number=bisection(n,m,a,b,error);
        z.append(temp)        
        # print('222',temp);
        #下一个零点
        a=z[k]+h;
        b=a+h;
        #这一步的含义
        number_bisection=number_bisection+number;
    print("二分法平均迭代次数",number_bisection/(k+1))
    return z
    





