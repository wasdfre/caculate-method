function a = legendreinterpolationcoefficients( xi,yi )

N=length(xi)-1;

L=zeros(N+1,N+1);

for j=1:N+1
    x=xi(j);
    k=0;
        L(1+k,j)=1;
    k=1;
        L(1+k,j)=x;
    for k=1:N-1
        L(1+k+1,j)=1/(k+1)*((2*k+1)*x*L(1+k,j)-k*L(1+k-1,j));
    end
end

a=zeros(1,N+1);
for k=0:N-1
   for j=1:N+1
       a(1+k)=a(1+k)+yi(j)*L(1+k,j)/L(1+N,j)^2;
   end
   a(1+k)=a(1+k)*(2*k+1)/(N*(N+1));
end

for j=1:N+1
   a(1+N)=a(1+N)+yi(j)/L(1+N,j);
end
a(1+N)=a(1+N)/(N+1);

end

