clear

N=20;
M=8;

x=-1:0.01:1;
y0=x*0;
y=y0;

for k=1:201
    y(k)=legendre(N,M,x(k));
end

subplot(1,2,1)
hold on
plot(x,y0)
plot(x,y)

subplot(1,2,2)
hold on
plot(x,y0)
plot(x,y)

set(gca,'YLim',[1.1*min(y),2*abs(min(y))]);

