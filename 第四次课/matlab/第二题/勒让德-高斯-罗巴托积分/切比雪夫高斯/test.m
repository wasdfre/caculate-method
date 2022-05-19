
clear

format long

N=80;

%勒让德高斯点
x=legendregauss(N+1,0);     
w=zeros(1,N+1);
for k=1:N+1
   w(k)=2/((1-x(k)^2)*(legendre(N+1,1,x(k)))^2);          
end

y=1./(1+25*x.^2);
I=y*w';                                 
error_le_gauss=abs(I-2/5*atan(5));


%勒让德高斯罗巴托点
x_lobatto=[-1,legendregauss(N,1),1];      
w_lobatto=zeros(1,N+1);
for k=1:N+1
   w_lobatto(k)=2/N/(N+1)/(legendre(N,0,x_lobatto(k)))^2;           
end

y_lobatto=1./(1+25*x_lobatto.^2);
I_lobatto=y_lobatto*w_lobatto';           
le_error_gauss_lobatto=abs(I_lobatto-2/5*atan(5));


N=1e2;
p=0:N;%从0开始

%切比雪夫高斯点
%求零点
x_gauss=cos(pi*(2*p+1)/(2*N+2));
%求函数值,注意权函数
par_fun=sqrt(1-x_gauss.^2);
y_gauss=(1./(1+25*x_gauss.^2)).*par_fun;
%计算w
w=ones(1,N+1)*pi/(N+1);
%使用点乘方式计算积分
I_gauss=sum(y_gauss*w');
%比较误差
error_gauss=abs(I_gauss-2/5*atan(5));


%切比雪夫高斯罗巴托点
%求零点
x_gauss_lobatto=cos(pi*p/N);
%求函数值,注意权函数
par_fun=sqrt(1-x_gauss_lobatto.^2);
y_gauss_lobatto=(1./(1+25*x_gauss_lobatto.^2)).*par_fun;
%计算w
w=ones(1,N+1)*pi/N;
%使用点乘方式计算积分
I_gauss_lobatto=sum(y_gauss_lobatto*w');
%比较误差
error_gauss_lobatto=abs(I_gauss_lobatto-2/5*atan(5));



%P5 1.3简单多项式插值
%求x
x_1_3=-1+p*2./N;
%求y
y_1_3=1./(1+25*x_1_3.^2);
%梯形公式计算积分
I_1_3=(2/N)*(sum(y_1_3)-1/2*(y_1_3(1)+y_1_3(end)));
%计算误差-[]
error_1_3=abs(I_1_3-2/5*atan(5));

fprintf("勒让德高斯点误差为%g\n",error_le_gauss)
fprintf("勒让德高斯点罗巴托误差为%g\n",le_error_gauss_lobatto)
fprintf("切比雪夫高斯点误差为%g\n",error_gauss)
fprintf("切比雪夫高斯点罗巴托误差为%g\n",error_gauss_lobatto)
fprintf("梯形公式误差为%g\n",error_1_3)

