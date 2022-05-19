clear
% warning('off')
warning('on')
time0=cputime;

a=-1;b=1;

 N=10;
%N=100;

j=1:N-1;
t=[1,cos(pi*j/N),-1];
xi=[a+(b-a)/2*(t+1)];

yi=sin(pi*xi);%计算y值


xy=[xi;yi];%组合


x1=a:(b-a)/1000:b;%设定待求集
y1=polynomialinterpolation(xy,x1);%插值求点



plot(x1,y1)%绘制图像

time=cputime-time0%计算时间
   
yexact=sin(pi*x1);
error=max(abs(y1-yexact))%计算误差

