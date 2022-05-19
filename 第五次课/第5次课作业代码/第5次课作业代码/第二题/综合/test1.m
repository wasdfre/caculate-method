clear 
format long

time0=cputime;

N=32;
m=1;
x=[-1,legendregauss(N,m),1];          %���õ�-��˹-�ް��е�

F0=zeros(N+1,1);
F2=zeros(N+1,1);

for k=0:N
   F0(1+k)=sin(x(1+k))+x(1+k)^3;          %����0�׵�
   F2(1+k)=-sin(x(1+k))+6*x(1+k);          %����2�׵�
end


D1=DM_1(N);          %���õ�һ��΢�־���


F_2=D1^2*F0;          %����2�׵���ֵ��

error=norm(F_2-F2)          %����2�׵���ֵ��;�ȷ���ķ��������
CPUTIME=cputime-time0

