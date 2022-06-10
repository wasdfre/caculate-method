clear

p0=1;
q0=0;

T=500000;
tau=0.1;



p=zeros(T,1);
q=zeros(T,1);

p(1)=p0;
q(1)=q0;



for t=2:T
    
    pm=p0;
    qm=q0;
    
    measure=1;
    while(measure>1e-14)
        p2=(pm+p0)/2;
        q2=(qm+q0)/2;
        
        pn=p0+tau*(-(p2^2+q2^2)*q2);
        qn=q0+tau*((p2^2+q2^2)*p2);
        
        measure=abs(pn-pm)+abs(qn-qm);
        pm=pn;
        qm=qn;
    end
    

    p(t)=pn;
    q(t)=qn;

    
    p0=pm;
    q0=qm;    
    

    
end


plot(p,q)

xlabel('p','Fontsize', 20);
ylabel('q','Fontsize', 20);
title('Midpoint method','Fontsize', 20);
set(gca, 'Fontsize', 20);

R=p.^2+q.^2;
maxR=max(R)
minR=min(R)

errorR=maxR-minR
