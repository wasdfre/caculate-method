
syms x_input

f(x_input)=x_input^3-x_input-1;
df(x_input)=3*x_input^2-1;

left=-5;right=5;x0=0.5;
%#初始值
xi=x0;
%#误差限
error=1e-14;
%#迭代公式
x_temp=right;
num_iter=0;
while(abs(xi-x_temp)>error)
    x_temp=xi;
    %#计算斜率
    yi=f(xi);
    %# print(yi)
    dfx=df(xi);
    k=0;

    x_temp2=xi-(yi/dfx);
    while(abs(f(x_temp2))>abs(yi))
        x_temp2=xi-(2^(-k))*(yi/dfx);
        k=k+1;
        num_iter=num_iter+1;
        %# print(k)
    end
    xi=x_temp2;
    %# print(xi)
end

% x,num_iter=newtown_down_hill(-5,5,0.5)

fprintf('下山法迭代次数为%f次\n', num_iter);
fprintf('方程的根x*为%f\n', xi);
fprintf('f(x*)的值为%f\n', f(xi));
