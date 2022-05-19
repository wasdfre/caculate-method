function [x,N] = bisection(n,m,alpha,beta,error)

if alpha<beta
    a=alpha;
    b=beta;
else
    b=alpha;
    a=beta;
end
%直接计算次数，向上取整，与while的复杂度比较
N=ceil(log2((b-a)/error));

fa=legendre(n,m,a);

if abs(fa)<error
   x=a;
   return
end

if abs(legendre(n,m,b))<error
   x=b;
   return
end

for k=1:N
   c=(b+a)/2;
   fc=legendre(n,m,c);
   
   if abs(fc)<error
       x=c;
       return
   end
    
   if fc*fa<0
       b=c;
   else
       a=c;
       fa=fc;
   end
end

x=c;

end

