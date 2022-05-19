clear

time0=cputime;

% N=10;
N=160;



xi=[-1,legendregauss(N,1),1];              %�������õ¸�˹�ް��е�
yi=1./(1+25*xi.^2);


a=legendreinterpolationcoefficients(xi,yi);    %�������õ²�ֵϵ��


x1=-1:2/1e6:1;
y1=legendreinterpolation(a,x1);                %�������õ²�ֵ���


plot(x1,y1)

time=cputime-time0
   
yexact=1./(1+25*x1.^2);
error=max(abs(y1-yexact))

