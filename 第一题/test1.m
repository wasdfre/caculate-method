clear 
%format long

N=10;
m=0;

time1=cputime;
x_bisection=legendregauss_bisection(N,m);                 %二分法
time2=cputime;
time_bisection=time2-time1;

x_Newton=legendregauss_Newton(N,m);                       %牛顿法
time3=cputime;
time_Newton=time3-time2;

error_bisection=0;
for k=1:N-m
    error_bisection=abs(legendre(N,m,x_bisection(k)))+error_bisection;
end
error_bisection=error_bisection/k;

error_Newton=0;
for k=1:N-m
    error_Newton=abs(legendre(N,m,x_Newton(k)))+error_Newton;
end
error_Newton=error_Newton/k;
fprintf("二分法需要时间为%f\n",time_bisection)
fprintf("牛顿法需要时间为%f\n",time_Newton)
fprintf("二分法平均误差为%g\n",error_bisection)
fprintf("牛顿法平均误差为%g\n",error_Newton)
