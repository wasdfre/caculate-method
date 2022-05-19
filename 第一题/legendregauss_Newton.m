function z=legendregauss_Newton(n,m)

if(n==0 || m>=n)
    z=[];
    return
end

error=1e-14;
h=n^(-2);
a=-1;
b=a+h;

number_newton=0;
for k=1:n-m
    
    legendre_a=legendre(n,m,a);
    legendre_b=legendre(n,m,b);
    while(legendre_a*legendre_b>0)
        a=b;
        legendre_a=legendre_b;
        
        b=a+h;
        legendre_b=legendre(n,m,b);
    end
   
   x=(a+b)/2;
   xright=b;
   while(abs(x-xright)>error)
        xright=x;
        x=x-legendre(n,m,x)/legendre(n,m+1,x);
        number_newton=number_newton+1;
   end
   z(k)=x;
   a=x+h;
   b=a+h;
end

fprintf('牛顿法平均迭代次数为%f次\n', number_newton/k);

end


