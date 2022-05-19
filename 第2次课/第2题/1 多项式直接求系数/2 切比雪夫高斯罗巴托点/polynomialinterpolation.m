function y = polynomialinterpolation(xy,x )



n=size(xy,2);

xy=xy';
x0=xy(:,1);
y0=xy(:,2);



m=length(x);
A=zeros(n);    

for k=1:n
    z=x0(k);
    A(k,1)=1;
    for j=2:n
        A(k,j)=A(k,j-1)*z;
    end
end

a=A\y0;


for l=1:m
    z=x(l);
    M=zeros(1,n);
    
    M(1)=1;
    for j=2:n
        M(j)=M(j-1)*z;
    end
    y(l)=sum(M'.*a);
%     y(l)=M*a;
end

end


