clear
%次数多反而时间少
T1=2e6;             %1运算次数，为什么要这个
T2=1e4;             %2运算次数

time0=cputime;      %记录cpu时间

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n1=1e10;            
for j=1:T1          %算法1
    e1=(1+1/n1)^n1; %n次方的方式，但是好像算了太多次了吧
end
time1=cputime;      %记录cpu时间

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


n2=9;
for j=1:T2          %算法2
    ff=Factorial(n2);%阶乘
    e2=1;           %初始值
    for k=1:n2      
       e2=e2+1/ff(k);%级数计算 
    end
end
time2=cputime;       %记录cpu时间

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cputime1=time1-time0 %第一个运算时间
e1
error1=abs(exp(1)-e1)%绝对误差限


cputime2=time2-time1 %第一个运算时间
e2
error2=abs(exp(1)-e2)%绝对误差限