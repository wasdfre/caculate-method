clear


syms xi
f(xi)=xi^3-xi-1;


x=[0.5,0.6];      %两个初始点
eps=1e-14;

fx=double(f(x(2)));

number_iteration=0;
while(abs(fx(1))>eps)

    fx=[double(f(x(1))),fx];
    x=[x(1)-double(f(x(1)))/(fx(1)-fx(2))*(x(1)-x(2)),x];   %式4.16
    
    number_iteration=number_iteration+1;
end

fprintf('弦截法迭代次数为%f次\n', number_iteration);
fprintf('方程的根x*为%f\n', x(1));
fprintf('f(x*)的值为%f\n', fx(1));


