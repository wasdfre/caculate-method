function x = jacobi_inv( A,b )
%JACOBI_INV 用jacobi迭代法解Ax=b

N=size(A,1);


x0=b;
x=zeros(N,1);

for k=1:N
    x(k)=1/A(k,k)*(b(k)-A(k,:)*x0+A(k,k)*x0(k));
end




while(norm(x-x0)>1e-10)
    x0=x;
    for k=1:N
        x(k)=1/A(k,k)*(b(k)-A(k,:)*x0+A(k,k)*x0(k));
    end
end


end

