clear
time0=cputime;

a=-5;
b=5;

K=4;

aa=a:(b-a)/K:b;              %先把[a,b]分成K份，对每个小区间用N次牛顿插值

N=32;

t=[-1,legendregauss(N,1),1];              %勒让德-高斯-罗巴托点
% j=1:N-1;
% t=[1,cos(pi*j/N),-1];              %切比雪夫-高斯-罗巴托点

x=[];
y=[];
for k=1:K
    x0=[aa(k)+(aa(k+1)-aa(k))/2*(t+1)];
    y0=1./(1+x0.^2);
    x1=aa(k):(aa(k+1)-aa(k))/(N*10):aa(k+1);       %加密10倍检验
    
    y1=newtoninterpolation(x0,y0,x1);              %牛顿插值（差商表法）
    x=[x,x1];
    y=[y,y1];
end

plot(x,y)

time=cputime-time0
   
yexact=1./(1+x.^2);
error=norm(y-yexact)
