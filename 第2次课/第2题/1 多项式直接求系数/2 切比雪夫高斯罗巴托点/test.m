clear
% warning('off')
warning('on')
time0=cputime;

a=-1;b=1;

N=10;
%N=100;%给定定点集个数


j=1:N-1;  %待求点的等分，N-1个
t=[1,cos(pi*j/N),-1];%设定步长，总N+1个数
xi=[a+(b-a)/2*(t+1)];%平移区间

yi=1./(1+25*xi.^2);%计算y值


xy=[xi;yi];


x1=a:(b-a)/1000:b;
y1=polynomialinterpolation(xy,x1);



plot(x1,y1)

time=cputime-time0
   
yexact=1./(1+25*x1.^2);
error=max(abs(y1-yexact))

