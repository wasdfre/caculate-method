clear 
format long

time0=cputime;

N=32;

j=[0:1:N]; 
x=[cos(pi*j/N)];          %�б�ѩ��-��˹-�ް��е㣬Ҳ���Ի���������

F0=zeros(N+1,1);
F2=zeros(N+1,1);

for k=0:N
   F0(1+k)=sin(x(1+k))+x(1+k)^3;          %����0�׵�
   F2(1+k)=-sin(x(1+k))+6*x(1+k);          %����2�׵�
end


D2=DM(2,N,x);          %�������ն���΢�־���

F_2=D2*F0;          %����2�׵���ֵ��

error=norm(F_2-F2)          %����2�׵���ֵ��;�ȷ���ķ��������
CPUTIME=cputime-time0



% l=4;k*sin(k*acos(x(l)))/sqrt(1-x(l)^2)
% ee=0.000000001;
% (cos(k*acos(x(l)+ee))-cos(k*acos(x(l))))/ee

