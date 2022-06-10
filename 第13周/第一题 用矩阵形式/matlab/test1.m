clear

N=100;

A=-2*eye(N);
for k=1:N-1
    A(k,k+1)=1;
    A(k+1,k)=1;
end
% b=eye(N);
b=ones(N,1);



X=A\b;

time0=cputime;

x_jacobi=jacobi_inv(A,b);
time1=cputime;

x_gaussseidel=gaussseidel_inv(A,b);
time2=cputime;

x_SOR=SOR_inv(A,b,1.2);
time3=cputime;


time_jacobi=time1-time0;
time_gaussseidel=time2-time1;
time_SOR=time3-time2;

error_jacobi=norm(X-x_jacobi);
error_gaussseidel=norm(X-x_gaussseidel);
error_SOR=norm(X-x_SOR);



fprintf('       雅克比迭代时间为%f', time_jacobi);
fprintf('    误差为%e\n', error_jacobi);
fprintf('    高斯赛德尔迭代时间为%f', time_gaussseidel);
fprintf('    误差为%e\n', error_gaussseidel);
fprintf('           SOR迭代时间为%f', time_SOR);
fprintf('    误差为%e\n', error_SOR);


