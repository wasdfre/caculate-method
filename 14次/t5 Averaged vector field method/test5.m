clear

p0=1;
q0=0;

T=5000000;
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
        
        %利用辛普森公式计算积分(仅作为展示,根据实际问题采用高阶数值积分)
        pn=p0-tau*((pm^2+qm^2)*qm+4*(p2^2+q2^2)*q2+(p0^2+q0^2)*q0)/6;
        qn=q0+tau*((pm^2+qm^2)*pm+4*(p2^2+q2^2)*p2+(p0^2+q0^2)*p0)/6;
        
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
title('Averaged vector field method','Fontsize', 20);
set(gca, 'Fontsize', 20);

% 哈密尔顿能量是1/4*(p.^2+q.^2).^2
R=p.^2+q.^2;
maxR=max(R)
minR=min(R)

errorR=maxR-minR
