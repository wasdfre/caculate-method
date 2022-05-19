%构建等分插值点
N=3000;
xi=[-1:2/N:1];
yi=(sin(pi*xi)+xi.^3)';
%构建微分矩阵
h=2/N;
D=zeros(N+1);
D(1,1)=-3;    D(1,2)=4;     D(1,3)=-1;
D(N+1,N-1)=1; D(N+1,N)=-4; D(N+1,N+1)=3;
for i=2:N
    D(i,i-1)=-1;
    D(i,i+1)=1;
end
D=D/(2*h);
%构建二阶微分矩阵
D2=D*D;
%计算结果
yd2=D2*yi;
%误差分析
yd2exact=(-sin(pi*xi)*pi^2+6*xi)';   
error_d2=norm(yd2-yd2exact) 


