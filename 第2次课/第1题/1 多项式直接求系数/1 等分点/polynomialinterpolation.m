function y = polynomialinterpolation(xy,x )



n=size(xy,2);  %定点长度，第二个值吗？

xy=xy';        %转置为列向量
x0=xy(:,1);    %获取x，y
y0=xy(:,2);



m=length(x);    %获取待求长度
A=zeros(n);     %获取设定A值，n*n吧

for k=1:n       %这里的n代表个数，从1开始，还是从0
    z=x0(k);    %设定X矩阵
    A(k,1)=1;   %第一个是1
    for j=2:n
        A(k,j)=A(k,j-1)*z;%后面依次乘x
    end
end

a=A\y0;          %代表左除A


for l=1:m        %待求长度
    z=x(l);      %获取对应x
    M=zeros(1,n);%x的向量
    
    M(1)=1;      %第一个
    for j=2:n
        M(j)=M(j-1)*z;%依次构造
    end
    y(l)=sum(M'.*a);%注意转置，点乘
%     y(l)=M*a;
end

end


