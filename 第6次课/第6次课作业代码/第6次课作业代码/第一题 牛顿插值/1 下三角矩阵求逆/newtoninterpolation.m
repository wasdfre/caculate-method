function y = newtoninterpolation(x0,y0,x )

n=length(x0);
m=length(x);
A=zeros(n);    
A(:,1)=1;
for k=2:n
   j=2;
   A(k,j)=x0(k)-x0(1);
   for j=3:k
       A(k,j)=A(k,j-1)*(x0(k)-x0(j-1));
   end
end
a=invlowertriangular(A,y0')
% a=A\y0';

for l=1:m
    z=x(l);
    M=zeros(1,n);
    
    M(1)=1;
    for j=2:n
        M(j)=M(j-1)*(z-x0(j-1));
    end
%     y(l)=sum(M'.*a);
    y(l)=M*a;
end

end


