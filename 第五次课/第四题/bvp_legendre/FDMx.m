function d = FDMx( M,N,xi,alpha )
c=zeros(N+1,N+1,M+1);
c(0+1,0+1,0+1)=1;
c1=1;
for n=1:N
    c2=1;
    for nu=0:n-1
        c3=alpha(n+1)-alpha(nu+1);
        c2=c2*c3;
        m=0;
            c(n+1,nu+1,m+1)=((alpha(n+1)-xi)*c(n-1+1,nu+1,m+1))/c3;
        for m=1:M
            c(n+1,nu+1,m+1)=((alpha(n+1)-xi)*c(n-1+1,nu+1,m+1)-m*c(n-1+1,nu+1,m-1+1))/c3;
        end
    end
    m=0;
        c(n+1,n+1,m+1)=c1*(-(alpha(n-1+1)-xi)*c(n-1+1,n-1+1,m+1))/c2; 
    for m=1:M
       c(n+1,n+1,m+1)=c1*(m*c(n-1+1,n-1+1,m-1+1)-(alpha(n-1+1)-xi)*c(n-1+1,n-1+1,m+1))/c2; 
    end
    c1=c2;
end

for j=0:N
   d(j+1)=c(N+1,j+1,M+1); 
end

end

