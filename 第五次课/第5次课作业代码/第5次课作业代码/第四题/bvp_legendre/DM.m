function Dm = DM( m,N,x )

for j=0:N
   xi=x(j+1);
   d=FDMx(m,N,xi,x);
   for nu=0:N
      Dm(j+1,nu+1)=d(nu+1); 
   end
end



end

