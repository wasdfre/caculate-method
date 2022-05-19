function d=DM_1(N)
jj=[0:1:N]; 
x=[cos(pi*jj/N)];
c=[2 ones(1,N-1) 2];

d=zeros(N+1,N+1);
for l=1:N+1
    for j=1:N+1
        if l==1 || l==N+1
            for k=1:N 
                d(l,j)=1/c(k+1)*(x(l))^(k-1)*k^2*cos(k*acos(x(j)))+d(l,j);
            end
        else
            for k=0:N
                d(l,j)=1/c(k+1)*k*sin(k*acos(x(l)))/sqrt(1-x(l)^2)*cos(k*acos(x(j)))+d(l,j);
            end
        end
        d(l,j)=d(l,j)*2/N/c(j);
    end 
end

