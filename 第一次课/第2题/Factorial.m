function y = Factorial( n ) %y是一个函数
global y %y又是变量
y=zeros(n,1); %y设定y为n空向量

f(n);%调用fn

end

function z = f( n )%fn
global y %又是y
if(n==1)%递归
    z=1;
else
    z=n*f(n-1);
end

y(n)=z;%保存z？
    
end
