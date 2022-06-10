clear

p0=1;
q0=0;

T=50000;
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

        
        %��������ɭ��ʽ�������(����Ϊչʾ,����ʵ��������ø߽���ֵ����)
        pn=p0-tau*((pm^4+qm^4)*qm+(p0^4+q0^4)*q0)/2;
        qn=q0+tau*((pm^4+qm^4)*pm+(p0^4+q0^4)*p0)/2;
        
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

% ���ܶ���������1/4*(p.^2+q.^2).^2
R=p.^2+q.^2;
maxR=max(R)
minR=min(R)

errorR=maxR-minR
