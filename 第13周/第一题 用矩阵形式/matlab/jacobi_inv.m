function x = jacobi_inv( A,b )
%JACOBI_INV 用jacobi迭代法解Ax=b

N=size(A,1);


D=diag(diag(A,0));    %求矩阵A的第1条对角线的元素。
L=-tril(A,-1);    %求矩阵A的第-1条对角线以下的元素。
U=-triu(A,1);    %求矩阵A的第1条对角线以上的元素。

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

