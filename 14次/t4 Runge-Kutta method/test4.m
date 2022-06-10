function main()


T=500000;
tau=0.1;

p=zeros(T,1);
q=zeros(T,1);

p(1)=1;
q(1)=0;

N=1;
yn=[1;0];

for t=2:T*N
    
    y0=yn;
    
    k1=f(y0);
    k2=f(y0+1/2*tau*k1);
    k3=f(y0+1/2*tau*k2);
    k4=f(y0+tau*k3);
    
    
    
    yn=y0+tau/6*(k1+2*k2+2*k3+k4);
    
    if(mod(t,N)==0)
        p(t/N)=yn(1);
        q(t/N)=yn(2);
    end
    
end


plot(p,q)

xlabel('p','Fontsize', 20);
ylabel('q','Fontsize', 20);
title('Runge-Kutta method','Fontsize', 20);
set(gca, 'Fontsize', 20);

R=p.^2+q.^2;
maxR=max(R)
minR=min(R)

errorR=maxR-minR


end

function y=f(y0)

    p=y0(1);
    q=y0(2);
    y=zeros(2,1);
    y(1)=-(p^2+q^2)*q;
    y(2)=(p^2+q^2)*p;

end
