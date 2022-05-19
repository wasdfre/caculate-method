function d = DM_1( N )
m=1;
x=[-1,legendregauss(N,m),1];
d=zeros(N+1,N+1);
for l=0:N
    for j=0:N
        for k=0:N-1 
            d(l+1,j+1)=(2*k+1)*legendre(k,0,x(j+1))/(legendre(N,0,x(j+1)))^2*legendre(k,1,x(l+1))+d(l+1,j+1);
        end
        d(l+1,j+1)=d(l+1,j+1)/(N*(N+1));
        d(l+1,j+1)=d(l+1,j+1)+1/(N+1)*legendre(N,1,x(l+1))/legendre(N,0,x(j+1));
    end 
end

