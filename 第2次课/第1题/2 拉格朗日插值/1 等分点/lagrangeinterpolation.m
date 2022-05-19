function y = lagrangeinterpolation(x0,y0,x )
n=length(x0);%获取长度
m=length(x);

L0=zeros(n,1);%计算l值，初始化l0是n，1

for k=1:n
     L=1;
     for j=1:n
         if j~=k%不等于下的两个乘积
             L=L/(x0(k)-x0(j));%下半部分
         end
     end
     L0(k)=L;
end


for l=1:m
   z=x(l);
   s=0;
   for k=1:n
      L=L0(k);
      for j=1:n
         if j~=k
            L=L*(z-x0(j));%上半部分
         end
      end
      s=s+L*y0(k);
   end
   y(l)=s;
end


end

