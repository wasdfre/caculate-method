clear

N=32;
epsilon=1;
cminus=exp(-5)+sin(1);
cplus=exp(5)+sin(1);
x=[-1,legendregauss(N,1),1];                %勒让德-高斯-罗巴托点

D1=DM(1,N,x);                %一阶微分矩阵（利用拉格朗日插值函数求导）
D2=DM(2,N,x);                %二阶微分矩阵（利用拉格朗日插值函数求导）

ue=zeros(N+1,1);
F=zeros(N+1,1);
P=zeros(N+1,N+1);
Q=zeros(N+1,N+1);

UE=zeros(N-1,1);
U0=zeros(N+1,1);
F0=zeros(N-1,1);
F1=zeros(N-1,1);
A1=zeros(N-1,N-1);
A0=zeros(N-1,N+1);

for k=1:N+1
    P(k,k)=p(x(k));
    Q(k,k)=q(x(k));
    
    F(k,1)=f(x(k));
    ue(k,1)=uexact(x(k));                %精确解
    
end

A=epsilon*D2+P*D1+Q;                %AU=F未考虑边界条件
A0(1:N-1,1:N+1)=A(2:N,1:N+1);
A1(1:N-1,1:N-1)=A(2:N,2:N);
F1(1:N-1)=F(2:N);
U0(1)=cminus;
U0(N+1)=cplus;
F0=A0*U0;

%A1*U1=F1-F0, 其中U1为U去掉U(1)和U(N+1)


[LL,UU,PP]=lu(A1);
U1=UU\(LL\PP*(F1-F0));       %利用PLU分解解线性方程组，等价于下一行求逆的式子
% U1=inv(A1)*(F1-F0);

UE(1:N-1)=ue(2:N);       %去掉边界条件的精确解


error=max(abs(U1-UE));
fprintf(1,'%16.0f    %13.3e',[N;error]);

U=U0;
U(2:N)=U1(:);
plot(x,U)