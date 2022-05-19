function y = legendreinterpolation(a,x )

N=length(a)-1;
M=length(x);


y=zeros(1,M);

for m=1:M
    L=zeros(N+1,1);
    z=x(m);
    k=0;
        L(1+k)=1;
    k=1;
        L(1+k)=z;
    for k=1:N-1
        L(1+k+1)=1/(k+1)*((2*k+1)*z*L(1+k)-k*L(1+k-1));
    end
    
    y(m)=a*L;
end


end

