function z=legendregauss(n,m)

%n=7;
%m=0;
error=1e-10;
h=n^(-2);
a=-1;

for k=1:n-m
   b=a+h;
   while(legendre(n,m,a)*legendre(n,m,b)>0)
        a=b;
        b=a+h;
   end
   x=(a+b)/2;
   xright=b;
   while(abs(x-xright)>error)
        xright=x;
        x=x-legendre(n,m,x)/legendre(n,m+1,x);
   end
   z(k)=x;
   a=x+h;
end


