clear

N=100000;               %设定分割量
x=0:1/N:1;              %在区间上建立分割点，从0开始
dx=zeros(N,1);          %dx值存储向
y=zeros(N,1);           %y值存储向量。

for k=1:N 
   y(k)=exp(x(k));      %对应y值
   dx(k)=x(k+1)-x(k);   %对应dx
end

I=sum(y.*dx);           %内积的方式求和

I_exact=exp(1)-1        %计算真实值
I_num=I                 %保留计算值
error=abs(I_exact-I_num)%计算绝对误差限




