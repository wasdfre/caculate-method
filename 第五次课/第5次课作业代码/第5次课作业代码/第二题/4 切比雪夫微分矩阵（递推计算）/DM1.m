function d=DM1(N)
j=[0:1:N]; 
x=[cos(pi*j/N)];
c=[2 ones(1,N-1) 2];
d=zeros(N+1,N+1);
for k=1:N+1
   for j=1:N+2-k
       if(j==1 && k==1)
           d(j,k)=(2*N^2+1)/6;
       elseif(j==N+1 && k==N+1)
           d(j,k)=-d(1,1);
       elseif(j==k)
           d(j,k)=-x(k)/(2*(1-x(k)^2));
       else
           d(j,k)=c(j)*(-1)^(j+k)/(c(k)*(x(j)-x(k)));    
       end
   end
end
for k=2:N+1
   for j=N+3-k:N+1
      d(k,j)=-d(N-k+2,N-j+2); 
   end
end

