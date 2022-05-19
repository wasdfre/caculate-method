function y = newtoninterpolation(x0,y0,x )

n=length(x0);
m=length(x);
A=zeros(n);    %������̱�
A(:,1)=y0;      %���̱���һ��Ϊy0
for j=2:n               %jΪ�б�
    for i=1:(n-j+1)     %iΪ�б�
        A(i,j)=(A(i,j-1)-A(i+1,j-1))/(x0(i)-x0(i+j-1));   %������̱�
    end
end
%���ݲ��̱�,���Ӧ��ţ�ٲ�ֵ����ʽ��x0=x(l)����ֵy(l)

a=A(1,:)';

for l=1:m
    z=x(l);
    M=zeros(1,n);
    
    M(1)=1;
    for j=2:n
        M(j)=M(j-1)*(z-x0(j-1));
    end
    y(l)=sum(M'.*a);
%     y(l)=M*a;
end

end


