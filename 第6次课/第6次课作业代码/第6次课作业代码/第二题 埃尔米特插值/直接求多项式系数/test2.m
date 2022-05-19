clear
warning('off')
% warning('on')
time0=cputime;
%给定区间范围
a=-5;
b=5;
%给定划分区间数
K=8;

aa=a:(b-a)/K:b;              %先把[a,b]分成K份，对每个小区间进行埃尔米特插值
%给定每个区间待求点个数
N=2^5;

%-1,1切比雪夫-高斯-罗巴托
j=1:N-1;
t=[1,cos(pi*j/N),-1];
%分区间计算
x=[];
y=[];
for k=1:K
    %区间变换
    x0=[aa(k)+(aa(k+1)-aa(k))/2*(t+1)];
    %计算y值
    y0=1./(1+x0.^2);
    z0=x0*0;                     %0阶导
    xy=[x0;z0;y0];              %[x,z,y]:x为自变量，y为函数值，z为几阶导数
    %随机生成导数插值条件
    rand_index = randperm(N+1);%随机整数排列
    dram_rand_index = rand_index(1:floor(N/2));%获取一半
    %获取对应x
    xx0=x0(dram_rand_index);
    %获取对应导数值
    yy0=-2*xx0.*(1+xx0.^2).^(-2);       %一阶导精确解
    zz0=xx0*0+1;                     %一阶导
    xy=[xy,[xx0;zz0;yy0]];
    
    
    rand_index = randperm(floor(N/2));
    dram_rand_index = rand_index(1:floor(N/4));
    xx0=xx0(dram_rand_index);
    yy0=-2*(1+xx0.^2).^(-2)+8*(xx0.^2).*(1+xx0.^2).^(-3);       %二阶导精确解
    zz0=xx0*0+2;                     %二阶导
    xy=[xy,[xx0;zz0;yy0]];
    
    
    rand_index = randperm(floor(N/4));
    dram_rand_index = rand_index(1:floor(N/8));
    xx0=xx0(dram_rand_index);
    yy0=24*xx0.*(1+xx0.^2).^(-3)-48*(xx0.^3).*(1+xx0.^2).^(-4);       %三阶导精确解
    zz0=xx0*0+3;                     %三阶导
    xy=[xy,[xx0;zz0;yy0]];
   
    rand_index = randperm(floor(N/8));
    dram_rand_index = rand_index(1:floor(N/16));
    xx0=xx0(dram_rand_index);
    yy0=24*(1+xx0.^2).^(-3)-288*(xx0.^2).*(1+xx0.^2).^(-4)+384*(xx0.^4).*(1+xx0.^2).^(-5);       %四阶导精确解
    zz0=xx0*0+4;                     %四阶导
    xy=[xy,[xx0;zz0;yy0]];
    
    
    
    
    x1=aa(k):(aa(k+1)-aa(k))/(N*10):aa(k+1);       %加密10倍检验
    y1=polynomialinterpolation(xy,x1);             %利用多项式直接求系数

    x=[x,x1];
    y=[y,y1];
end

plot(x,y)

time=cputime-time0
   
yexact=1./(1+x.^2);
error=norm(y-yexact)
