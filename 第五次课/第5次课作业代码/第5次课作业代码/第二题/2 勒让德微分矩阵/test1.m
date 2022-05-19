clear 
format long

time0=cputime;

N=32;
m=1;
x=[-1,legendregauss(N,m),1];          %勒让德-高斯-罗巴托点

F0=zeros(N+1,1);
F2=zeros(N+1,1);

for k=0:N
   F0(1+k)=sin(x(1+k))+x(1+k)^3;          %函数0阶导
   F2(1+k)=-sin(x(1+k))+6*x(1+k);          %函数2阶导
end


D1=DM_1(N);          %勒让德一阶微分矩阵


F_2=D1^2*F0;          %函数2阶导数值解

error=norm(F_2-F2)          %函数2阶导数值解和精确解差的范数，误差
CPUTIME=cputime-time0

