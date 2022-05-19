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

yi=sin(pi*xi);


xy=[xi;yi];


x1=a:(b-a)/1000:b;
y1=lagrangeinterpolation(xi,yi,x1);



plot(x1,y1)

time=cputime-time0
   
yexact=sin(pi*x1);
error=max(abs(y1-yexact))

