function y = polynomialinterpolation(xy,x )



n=size(xy,2);
%指定n值
xy=xy';%作用是转置，也就是开始时行向量
x0=xy(:,1);%给定点x0
y0=xy(:,2);%给定点y0



m=length(x);%x为待求长度
A=zeros(n); %A向量，只给一值注意

for k=1:n
    z=x0(k);%给定x
    A(k,1)=1;
    for j=2:n
        A(k,j)=A(k,j-1)*z;
    end
end

a=A\y0;


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


