clear
warning('off')
% warning('on')
time0=cputime;
%�������䷶Χ
a=-5;
b=5;
%��������������
K=8;

aa=a:(b-a)/K:b;              %�Ȱ�[a,b]�ֳ�K�ݣ���ÿ��С������а������ز�ֵ
%����ÿ�������������
N=2^5;

%-1,1�б�ѩ��-��˹-�ް���
j=1:N-1;
t=[1,cos(pi*j/N),-1];
%���������
x=[];
y=[];
for k=1:K
    %����任
    x0=[aa(k)+(aa(k+1)-aa(k))/2*(t+1)];
    %����yֵ
    y0=1./(1+x0.^2);
    z0=x0*0;                     %0�׵�
    xy=[x0;z0;y0];              %[x,z,y]:xΪ�Ա�����yΪ����ֵ��zΪ���׵���
    %������ɵ�����ֵ����
    rand_index = randperm(N+1);%�����������
    dram_rand_index = rand_index(1:floor(N/2));%��ȡһ��
    %��ȡ��Ӧx
    xx0=x0(dram_rand_index);
    %��ȡ��Ӧ����ֵ
    yy0=-2*xx0.*(1+xx0.^2).^(-2);       %һ�׵���ȷ��
    zz0=xx0*0+1;                     %һ�׵�
    xy=[xy,[xx0;zz0;yy0]];
    
    
    rand_index = randperm(floor(N/2));
    dram_rand_index = rand_index(1:floor(N/4));
    xx0=xx0(dram_rand_index);
    yy0=-2*(1+xx0.^2).^(-2)+8*(xx0.^2).*(1+xx0.^2).^(-3);       %���׵���ȷ��
    zz0=xx0*0+2;                     %���׵�
    xy=[xy,[xx0;zz0;yy0]];
    
    
    rand_index = randperm(floor(N/4));
    dram_rand_index = rand_index(1:floor(N/8));
    xx0=xx0(dram_rand_index);
    yy0=24*xx0.*(1+xx0.^2).^(-3)-48*(xx0.^3).*(1+xx0.^2).^(-4);       %���׵���ȷ��
    zz0=xx0*0+3;                     %���׵�
    xy=[xy,[xx0;zz0;yy0]];
   
    rand_index = randperm(floor(N/8));
    dram_rand_index = rand_index(1:floor(N/16));
    xx0=xx0(dram_rand_index);
    yy0=24*(1+xx0.^2).^(-3)-288*(xx0.^2).*(1+xx0.^2).^(-4)+384*(xx0.^4).*(1+xx0.^2).^(-5);       %�Ľ׵���ȷ��
    zz0=xx0*0+4;                     %�Ľ׵�
    xy=[xy,[xx0;zz0;yy0]];
    
    
    
    
    x1=aa(k):(aa(k+1)-aa(k))/(N*10):aa(k+1);       %����10������
    y1=polynomialinterpolation(xy,x1);             %���ö���ʽֱ����ϵ��

    x=[x,x1];
    y=[y,y1];
end

plot(x,y)

time=cputime-time0
   
yexact=1./(1+x.^2);
error=norm(y-yexact)
