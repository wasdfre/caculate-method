import numpy as np
def f(x):
    return 1/(1+x**2);

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

def legendre_lobatto_coff(x):
    #阶数
    N=len(x)-1;
    #系数
    W=np.zeros(N+1);
    for i in range(0,N+1):
       W[i]=1/(legendre(N,0,x[i])**2);
    W=2/(N*(N+1))*W;
    return W
#计算n阶勒让德，m阶导数的零点
def legendregauss(n,m):
    if n==0:
        return []
    z=[]
    error=1e-14
    h=n**(-2)
    a=-1
    b=a+h
    number_newton=0;
    for k in range(1,n-m+1):
        legendre_a=legendre(n,m,a)
        legendre_b=legendre(n,m,b)
        while(legendre_a*legendre_b>0):
            a=b
            legendre_a=legendre_b         
            b=a+h
            legendre_b=legendre(n,m,b)  
        x=(a+b)*0.5
        xright=b
        while(np.abs(x-xright)>error):
            xright=x
            x=x-legendre(n,m,x)/legendre(n,m+1,x)
            number_newton+=1;
        z.append(x)
        a=x+h
        b=a+h
    return np.array(z)
   
N=160;
a=-5;b=5;
#获得[-1,1]高斯罗巴托点
x=np.zeros(N+1)
x[1:-1]=legendregauss(N,1);
x[0]=-1;x[-1]=1;  

#求勒让德高斯罗巴托点积分系数
W=legendre_lobatto_coff(x); 

#给出积分点
left=a;right=b;
x_temp=left+1/2*(right-left)*(x+1);

#积分
y=f(x_temp);
#注意系数
res=(b-a)/2*sum(W*y);

#误差比较
error=abs(res-2*np.arctan(5));
print(error);