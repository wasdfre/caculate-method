clear

%点个数
N=64128;                    
%方程参数与边界
epsilon=1e-3;            
cminus=0;
cplus=1;
%切比雪夫-高斯-罗巴托点
j=[1:1:N-1]; 
x=[1,cos(pi*j/N),-1]';           
%切比雪夫一阶微分矩阵
D1=DM1(N);       
%用一阶微分矩阵的平方近似二阶微分矩阵         
D2=D1^2;                  

ue=zeros(N+1,1);%精确解存放
F=zeros(N+1,1);
P=zeros(N+1,N+1);
Q=zeros(N+1,N+1);

UE=zeros(N-1,1);%去掉边界条件精确解存放
U0=zeros(N+1,1);%y值存放处
F0=zeros(N-1,1);%被拆分(边界值)y值存放处
F1=zeros(N-1,1);%去掉边界值的y值存放处
A1=zeros(N-1,N-1);%拆掉左右与上下后主矩阵存放处
A0=zeros(N-1,N+1);%拆掉第一行与最后一行

for k=1:N+1
    P(k,k)=p(x(k));
    Q(k,k)=q(x(k));
    
    F(k,1)=f(x(k));
    ue(k,1)=uexact(x(k),epsilon);                %精确解
    
end

A=epsilon*D2+P*D1+Q;                %AU=F未考虑边界条件
A0(1:N-1,1:N+1)=A(2:N,1:N+1);
A1(1:N-1,1:N-1)=A(2:N,2:N);
F1(1:N-1)=F(2:N);
U0(1)=cplus;
U0(N+1)=cminus;
F0=A0*U0;

%A1*U1=F1-F0, 其中U1为U去掉U(1)和U(N+1)



[LL,UU,PP]=lu(A1);
U1=UU\(LL\PP*(F1-F0));       %利用PLU分解解线性方程组，等价于下一行求逆的式子
% U1=inv(A1)*(F1-F0);


UE(1:N-1)=ue(2:N);            %去掉边界条件的精确解
%误差分析
error=max(abs(U1-UE));
fprintf(1,'%16.0f    %13.3e',[N;error]);

U=U0;
U(2:N)=U1(:);
plot(x,U)