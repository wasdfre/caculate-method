clear all
% 参数
n=8;
m=1;

% #误差限
error=1e-14;

% 每个零点间距
h=n^(-2);

% 区间边界
left=-1;right=left+h;
% 存储零点
x=[];
% 统计零点个数
i=0;
%循环次数
number_iter=0;
for k = 1:n-m
    f_left=legendre(n,m,left);
    f_right=legendre(n,m,right);

    while(f_left*f_right>0)
        left=right;right=left+h;
        f_left=f_right;
        f_right=legendre(n,m,right);
    end
    iter_temp=0;

    xi=(left+right)/2;

    x_temp=right;
   while(abs(xi-x_temp)>error)
        x_temp=xi;
        xi=xi-legendre(n,m,xi)/legendre(n,m+1,xi);
        iter_temp=iter_temp+1;
   end
    left=xi+h;right=left+h;
    x=[x,xi];%添加元素
    number_iter=number_iter+iter_temp;
end

fprintf('牛顿法迭代次数为%f次\n', number_iter/(n-m));
fprintf('方程的根x*为%f\n',x);

