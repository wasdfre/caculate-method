clear

time0=cputime;

a=-1;b=1;

N=10;                  %给定定点集个数
% N=100;

xi=a:(b-a)/N:b;        %定点集x
yi=sin(pi*xi);         %定点集y


x1=a:(b-a)/1000:b;     %待求点的等分
y1=lagrangeinterpolation(xi,yi,x1);%插值



plot(x1,y1)%绘制图像

time=cputime-time0%计算时间
   
yexact=sin(pi*x1);
error=max(abs(y1-yexact))

