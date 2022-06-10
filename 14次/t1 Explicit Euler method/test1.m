clear

p=[1];
q=[0];

T=4500;
tau=0.01;

for t=1:T
    pn=p(1)+tau*(-(p(1)^2+q(1)^2)*q(1));
    qn=q(1)+tau*((p(1)^2+q(1)^2)*p(1));
    
    p=[pn,p];
    q=[qn,q];
end


plot(p,q)

xlabel('p','Fontsize', 20);
ylabel('q','Fontsize', 20);
title('Explicit Euler method','Fontsize', 20);
set(gca, 'Fontsize', 20);

R=p.^2+q.^2;
maxR=max(R)
minR=min(R)