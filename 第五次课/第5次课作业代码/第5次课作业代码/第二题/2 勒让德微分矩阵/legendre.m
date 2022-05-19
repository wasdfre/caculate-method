function r=legendre(n,m,x)

for j=0:m
   if(j==0)
      s(1+0,1+j)=1;
      s(1+1,1+j)=x;
      for k=1:n-1
        s(1+k+1,1+j)=((2*k+1)*x*s(1+k,1+j)-k*s(1+k-1,1+j))/(k+1);
      end
   else
       s(1+0,1+j)=0;
       if(j==1)
           s(1+1,1+j)=1;
       else
           s(1+1,1+j)=0;
       end
       for k=1:n-1
           s(1+k+1,1+j)=(2*k+1)*s(1+k,1+j-1)+s(1+k-1,1+j);
       end
   end
end
r=s(1+n,1+m);

