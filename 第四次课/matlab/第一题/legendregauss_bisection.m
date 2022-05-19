function z=legendregauss_bisection(n,m)

if(n==0 || m>=n)
    z=[];
    return
end

error=1e-18;
h=n^(-2);
a=-1;
b=a+h;


number_bisection=0;
for k=1:n-m
    legendre_a=legendre(n,m,a);
    legendre_b=legendre(n,m,b);
    while(legendre_a*legendre_b>0)
        a=b;
        legendre_a=legendre_b;
        
        b=a+h;
        legendre_b=legendre(n,m,b);
    end
    
   [z(k),number]=bisection(n,m,a,b,error);
   a=z(k)+h;
   b=a+h;
   
   number_bisection=number_bisection+number;
end

fprintf('二分法平均计算次数为%f次\n', number_bisection/k);

end

