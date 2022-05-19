function y = polynomialinterpolation(xy,x )


%这个是那个size？
n=size(xy,2);

xy=xy';
x0=xy(:,1);
y0=xy(:,3);
z=xy(:,2);


m=length(x);
A=zeros(n);    
%求解A
for k=1:n
    for j=1:n
        % j为多项式次数，z为求导次数
        [n1,n2]=Fa(j,z(k));
        A(k,j)=n1*x0(k)^(n2-1);
        %如果为nan，则定义为0
        if(isnan(A(k,j)))
            A(k,j)=0;
        end
    end
end
%求解A，直接使用矩阵解线性方程组的方式
a=A\y0;

%求解y
for l=1:m
    z=x(l);
    M=zeros(1,n);
    
    M(1)=1;
    for j=2:n
        M(j)=M(j-1)*z;
    end
    y(l)=sum(M'.*a);
%     y(l)=M*a;
end

end


