clear

%�����
N=64128;                    
%���̲�����߽�
epsilon=1e-3;            
cminus=0;
cplus=1;
%�б�ѩ��-��˹-�ް��е�
j=[1:1:N-1]; 
x=[1,cos(pi*j/N),-1]';           
%�б�ѩ��һ��΢�־���
D1=DM1(N);       
%��һ��΢�־����ƽ�����ƶ���΢�־���         
D2=D1^2;                  

ue=zeros(N+1,1);%��ȷ����
F=zeros(N+1,1);
P=zeros(N+1,N+1);
Q=zeros(N+1,N+1);

UE=zeros(N-1,1);%ȥ���߽�������ȷ����
U0=zeros(N+1,1);%yֵ��Ŵ�
F0=zeros(N-1,1);%�����(�߽�ֵ)yֵ��Ŵ�
F1=zeros(N-1,1);%ȥ���߽�ֵ��yֵ��Ŵ�
A1=zeros(N-1,N-1);%������������º��������Ŵ�
A0=zeros(N-1,N+1);%�����һ�������һ��

for k=1:N+1
    P(k,k)=p(x(k));
    Q(k,k)=q(x(k));
    
    F(k,1)=f(x(k));
    ue(k,1)=uexact(x(k),epsilon);                %��ȷ��
    
end

A=epsilon*D2+P*D1+Q;                %AU=Fδ���Ǳ߽�����
A0(1:N-1,1:N+1)=A(2:N,1:N+1);
A1(1:N-1,1:N-1)=A(2:N,2:N);
F1(1:N-1)=F(2:N);
U0(1)=cplus;
U0(N+1)=cminus;
F0=A0*U0;

%A1*U1=F1-F0, ����U1ΪUȥ��U(1)��U(N+1)



[LL,UU,PP]=lu(A1);
U1=UU\(LL\PP*(F1-F0));       %����PLU�ֽ�����Է����飬�ȼ�����һ�������ʽ��
% U1=inv(A1)*(F1-F0);


UE(1:N-1)=ue(2:N);            %ȥ���߽������ľ�ȷ��
%������
error=max(abs(U1-UE));
fprintf(1,'%16.0f    %13.3e',[N;error]);

U=U0;
U(2:N)=U1(:);
plot(x,U)