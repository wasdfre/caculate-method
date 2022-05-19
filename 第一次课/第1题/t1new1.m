clear

N=100000;
x=0:1/N:1;
dx=zeros(N,1);
y=zeros(N,1);

for k=1:N
    y(k)=exp(x(k))
    dx(k)=x(k+1)-x(k);
end

I=sum(y.*dx);
I_exact=exp(1)-1
I_num=I
error=abs(I_exact-I_num)