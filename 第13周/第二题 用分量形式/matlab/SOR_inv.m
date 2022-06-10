function x = SOR_inv( A,b,omega )
%SOR_INV �˴���ʾ�йش˺�����ժҪ


N=size(A,1);

x0=b;
x=zeros(N,1);

for k=1:N
    x(k)=x0(k)+omega/A(k,k)*(b(k)-A(k,1:k-1)*x(1:k-1)-A(k,k:N)*x0(k:N));
end


while(norm(x-x0)>1e-10)
    x0=x;
    for k=1:N
        x(k)=x0(k)+omega/A(k,k)*(b(k)-A(k,1:k-1)*x(1:k-1)-A(k,k:N)*x0(k:N));
    end
end





end

