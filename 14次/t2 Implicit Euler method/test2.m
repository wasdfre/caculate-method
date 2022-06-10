clear

p=[1];
q=[0];

T=4500;
tau=0.01;

pm=p(1);
qm=q(1);

for t=1:T
    
    measure=1;
    while(measure>1e-14)
        pn=p(1)+tau*(-(pm^2+qm^2)*qm);
        qn=q(1)+tau*((pm^2+qm^2)*pm);
        
        measure=abs(pn-pm)+abs(qn-qm);
        pm=pn;
        qm=qn;
    end
    
    p=[pn,p];
    q=[qn,q];
end


plot(p,q)

xlabel('p','Fontsize', 20);
ylabel('q','Fontsize', 20);
title('Implicit Euler method','Fontsize', 20);
set(gca, 'Fontsize', 20);

R=p.^2+q.^2;
maxR=max(R)
minR=min(R)
