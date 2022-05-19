clear


syms xi
f(xi)=xi^3-xi-1;


x=[0.5,0.6];      %������ʼ��
eps=1e-14;

fx=double(f(x(2)));

number_iteration=0;
while(abs(fx(1))>eps)

    fx=[double(f(x(1))),fx];
    x=[x(1)-double(f(x(1)))/(fx(1)-fx(2))*(x(1)-x(2)),x];   %ʽ4.16
    
    number_iteration=number_iteration+1;
end

fprintf('�ҽط���������Ϊ%f��\n', number_iteration);
fprintf('���̵ĸ�x*Ϊ%f\n', x(1));
fprintf('f(x*)��ֵΪ%f\n', fx(1));


