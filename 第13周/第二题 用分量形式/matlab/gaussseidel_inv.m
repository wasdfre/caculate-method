function x = gaussseidel_inv( A,b )
%GAUSSSEIDEL_INV 此处显示有关此函数的摘要

N=size(A,1);

x0=b;
x=zeros(N,1);

for k=1:N
    x(k)=1/A(k,k)*(b(k)-A(k,1:k-1)*x(1:k-1)-A(k,k+1:N)*x0(k+1:N));
%     x(k)=x0(k)+1/A(k,k)*(b(k)-A(k,1:k-1)*x(1:k-1)-A(k,k:N)*x0(k:N));
end


while(norm(x-x0)>1e-10)
    x0=x;
    for k=1:N
        x(k)=x0(k)+1/A(k,k)*(b(k)-A(k,1:k-1)*x(1:k-1)-A(k,k:N)*x0(k:N));
    end
end


end

