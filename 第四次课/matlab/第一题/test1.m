clear 


N=10;
m=0;

time1=cputime;
x_bisection=legendregauss_bisection(N,m);                 %���ַ�
time2=cputime;
time_bisection=time2-time1

x_Newton=legendregauss_Newton(N,m);                       %ţ�ٷ�
time3=cputime;
time_Newton=time3-time2

error_bisection=0;
for k=1:N-m
    error_bisection=abs(legendre(N,m,x_bisection(k)))+error_bisection;
end
error_bisection=error_bisection/k

error_Newton=0;
for k=1:N-m
    error_Newton=abs(legendre(N,m,x_Newton(k)))+error_Newton;
end
error_Newton=error_Newton/k