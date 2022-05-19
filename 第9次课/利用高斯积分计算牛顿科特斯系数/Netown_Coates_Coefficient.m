clear
format long

% ���տα�108ҳ��3-1��ȡn=4, �����ϵ��
N=7;

% x1�Ǹ�˹�㣬w1�Ǹ�˹����ϵ��������Ϊ�����ø�˹���ּ���ţ�ٿ���˹ϵ����׼��
Nl=floor(N/2);
xl=legendregauss(Nl+1,0);
wl=zeros(1,Nl+1);
for k=1:Nl+1
   wl(k)=2/((1-xl(k)^2)*(legendre(Nl+1,1,xl(k)))^2);
end

% �����������ţ�ٿ���˹ϵ�����ο�106ҳ��ʽ(3.2),ȡb=1,a=-1
x=-1:2/N:1;        %�ȷֵ�
w=zeros(1,N+1);
for k=1:N+1
   x0=x;
   y0=zeros(1,N+1);
   y0(k)=1;
   yl=lagrangeinterpolation(x0,y0,xl);     %����ʽ����������������ղ�ֵ
   w(k)=yl*wl';
end


% ��һ����ֵ�������ӽ�����֤
y=1./(1+25*x.^2);
I=y*w';
error=abs(I-2/5*atan(5))

% ţ�ٿ���˹ϵ��
Newton_Coates_Coefficients=w/2
