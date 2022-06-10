function x = gaussseidel_inv( A,b )
%GAUSSSEIDEL_INV �˴���ʾ�йش˺�����ժҪ


N=size(A,1);


D=diag(diag(A,0));    %�����A�ĵ�1���Խ��ߵ�Ԫ�ء�
L=-tril(A,-1);    %�����A�ĵ�-1���Խ������µ�Ԫ�ء�
U=-triu(A,1);    %�����A�ĵ�1���Խ������ϵ�Ԫ�ء�

invDL=(D-L)\eye(N);
B=invDL*U;
g=invDL*b;

x0=g;
x=B*x0+g;

while(norm(x-x0)>1e-14)
    x0=x;
    x=B*x0+g;
end


end

