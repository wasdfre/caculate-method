clear
time0=cputime;

N=100;
%-1��1�ȷֵ�
x0=-1:2/N:1;              %�ȷֵ�
% j=1:N-1;
% x0=[1,cos(pi*j/N),-1];

y0=1./(1+25*x0.^2);

%-1��1�����
x=-1:2/N/10:1;
%Ĭ��Ϊ�������ձ߽�����
 pp=interp1(x0,y0,'spline','pp');       %����������ֵ��
%pp=csape(x0,y0,'periodic');            %����������ֵ�����ڱ߽�
%pp=csape(x0,y0,'second');              %����������ֵ
%pp=csape(x0,y0,'complete');              %����������ֵ���������ձ߽�
%�������ʽ
y=ppval(pp,x);


time=cputime-time0

plot(x,y)

yexact=1./(1+25*x.^2);
error=norm(y-yexact)

