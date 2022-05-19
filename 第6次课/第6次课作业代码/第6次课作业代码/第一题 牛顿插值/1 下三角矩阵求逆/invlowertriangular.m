function x = invlowertriangular( A,b )

N=length(b);
x=zeros(N,1);
x(1)=b(1)/A(1,1);
for k=2:N
    x(k)=(b(k)-A(k,1:k-1)*x(1:k-1))/A(k,k);
end

end

