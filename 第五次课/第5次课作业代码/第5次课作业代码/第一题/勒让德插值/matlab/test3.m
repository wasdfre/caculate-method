clear

time0=cputime;

% N=10;
N=160;



xi=[-1,legendregauss(N,1),1];              %计算勒让德高斯罗巴托点
yi=1./(1+25*xi.^2);


a=legendreinterpolationcoefficients(xi,yi);    %计算勒让德插值系数


x1=-1:2/1e6:1;
y1=legendreinterpolation(a,x1);                %计算勒让德插值结果


plot(x1,y1)

time=cputime-time0
   
yexact=1./(1+25*x1.^2);
error=max(abs(y1-yexact))

