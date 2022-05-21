function main()

N=64;
epsilon=1;
cminus=exp(-5)+sin(1);
cplus=exp(5)+sin(1);
j=[1:1:N-1]; 
x=[1,cos(pi*j/N),-1]';
D1=DM1(N);
D2=D1^2;

% U=zeros(N+1,1);
ue=zeros(N+1,1);
F=zeros(N+1,1);
P=zeros(N+1,N+1);
Q=zeros(N+1,N+1);

UE=zeros(N-1,1);
U0=zeros(N+1,1);
F0=zeros(N-1,1);
F1=zeros(N-1,1);
A1=zeros(N-1,N-1);
A0=zeros(N-1,N+1);

for k=1:N+1
    P(k,k)=p(x(k));
    Q(k,k)=q(x(k));
    
    F(k,1)=f(x(k));
    ue(k,1)=uexact(x(k));
    
end

A=epsilon*D2+P*D1+Q;
A0(1:N-1,1:N+1)=A(2:N,1:N+1);
A1(1:N-1,1:N-1)=A(2:N,2:N);
F1(1:N-1)=F(2:N);
U0(1)=cplus;
U0(N+1)=cminus;
F0=A0*U0;


% [LL,UU,PP]=lu(A1);

% U1=UU\(LL\PP*(F1-F0));
U1=inv(A1)*(F1-F0);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
A=A1;
b=F1-F0;

x=my_inv(A,b);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

error=norm(x-U1)

end

function d=DM1(N)
j=[0:1:N]; 
x=[cos(pi*j/N)];
c=[2 ones(1,N-1) 2];
for k=1:N+1
   for j=1:N+2-k
       if(j==1 && k==1)
           d(j,k)=(2*N^2+1)/6;
       elseif(j==N+1 && k==N+1)
           d(j,k)=-d(1,1);
       elseif(j==k)
           d(j,k)=-x(k)/(2*(1-x(k)^2));
       else
           d(j,k)=c(j)*(-1)^(j+k)/(c(k)*(x(j)-x(k)));    
       end
   end
end
for k=2:N+1
   for j=N+3-k:N+1
      d(k,j)=-d(N-k+2,N-j+2); 
   end
end
end
function f = f(x)

f=(24+5*x)*exp(5*x)+(2+2*x^2)*cos(x^2)-(4*x^2+1)*sin(x^2);

end
function p = p(x)

p=x;
end
function q = q(x)

q=-1;

end
function u = uexact(x)

u=exp(5*x)+sin(x^2);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function x = my_inv( A,b )
%解Ax=b

% [L,U,P]=lu(A); 列主元LU分解（PLU）
% x=U\(L\(P*b));


[P,L,U]=my_lup(A); %行主元LU分解(LUP)
x=P*(U\(L\b));
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

