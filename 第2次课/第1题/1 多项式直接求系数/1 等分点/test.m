clear
% warning('off')
warning('on')
time0=cputime;

a=-1;b=1;

N=10;                   %给定定点集个数
% N=100;

xi=a:(b-a)/N:b;         %步长为这个的等分店，ppt上为倒着给点
yi=sin(pi*xi);          %y值,但是为N+1个数


xy=[xi;yi];              %组合


x1=a:(b-a)/1000:b;       %待求点的等分
y1=polynomialinterpolation(xy,x1);%插值求点



plot(x1,y1)             %绘制图像

time=cputime-time0      %计算时间
   
yexact=sin(pi*x1);
error=max(abs(y1-yexact))%计算误差

