function x = jacobi_inv( A,b )
%JACOBI_INV ��jacobi��������Ax=b

N=size(A,1);


D=diag(diag(A,0));    %�����A�ĵ�1���Խ��ߵ�Ԫ�ء�
L=-tril(A,-1);    %�����A�ĵ�-1���Խ������µ�Ԫ�ء�
U=-triu(A,1);    %�����A�ĵ�1���Խ������ϵ�Ԫ�ء�

invD=D\eye(N);
B=invD*(L+U);
g=invD*b;

x0=g;
x=B*x0+g;

while(norm(x-x0)>1e-14)
    x0=x;
    x=B*x0+g;
end


end

