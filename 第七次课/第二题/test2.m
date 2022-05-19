clear

N=2000;


%generate random points in (-1,)]
xi=sort(rand(1,N)*2-1);
yi=1./(1+25*(xi.^2))+(rand(1,N)*2-1)*0.1;
% scatter(xi,yi,'red');hold on;


% generate X
L=25;
start=1;
X=zeros(N,L+1);
% X(:,1)=1;%x^0=1;
for i = 1:N
    for j =start:L
        X(i,j+1)=xi(i)^j;
    end
end


%calculate the A
Y=yi';
A=pinv(X'*X)*X'*Y;
%A=X\Y;
% scatter(xi,(X*A)','blue');

y_train_predict=(X*A)';

%generate xj
M=120;
x=sort(rand(1,M)*2-1);


%generate X_pre
X_pre=zeros(M,L+1);
for i = 1:M
    for j =start:L
        X_pre(i,j+1)=x(i)^j;
    end
end


%calculate y_pre
y_pre=(X_pre*A)';
%error
y_exact=1./(1+25*x.^2);
%average error
error=sqrt(sum((y_pre-y_exact).^2)/length(y_exact))

%训练集
subplot(2,1,1)
scatter(xi,yi,'blue');hold on
plot(xi,y_train_predict,'red');

%测试集
subplot(2,1,2)
plot(x,y_pre,'blue');hold on
scatter(x,y_exact,'red');
