clear
format long

% 对照课本108页表3-1中取n=4, 共五个系数
N=7;

% x1是高斯点，w1是高斯积分系数，这是为了利用高斯积分计算牛顿科特斯系数作准备
Nl=floor(N/2);
xl=legendregauss(Nl+1,0);
wl=zeros(1,Nl+1);
for k=1:Nl+1
   wl(k)=2/((1-xl(k)^2)*(legendre(Nl+1,1,xl(k)))^2);
end

% 计算出二倍的牛顿科特斯系数，参考106页公式(3.2),取b=1,a=-1
x=-1:2/N:1;        %等分点
w=zeros(1,N+1);
for k=1:N+1
   x0=x;
   y0=zeros(1,N+1);
   y0(k)=1;
   yl=lagrangeinterpolation(x0,y0,xl);     %多项式函数恒等于拉格朗日插值
   w(k)=yl*wl';
end


% 找一个数值积分例子进行验证
y=1./(1+25*x.^2);
I=y*w';
error=abs(I-2/5*atan(5))

% 牛顿科特斯系数
Newton_Coates_Coefficients=w/2
