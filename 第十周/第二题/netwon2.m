clear


syms xi
f(xi)=xi^3-xi-1;
f1(xi)=3*xi^2-1;

x=0.5;
eps=1e-14;

error=abs(double(f(x)));

number_iteration=0;
while(error>eps)

    x=[x(1)-double(f(x(1))/f1(x(1))),x]; 
    error=abs(double(f(x(1))));
    number_iteration=number_iteration+1;
end

fprintf('ţ�ٷ���������Ϊ%f��\n', number_iteration);
fprintf('���̵ĸ�x*Ϊ%f\n', x(1));
fprintf('f(x*)��ֵΪ%f\n', f(x(1)));













