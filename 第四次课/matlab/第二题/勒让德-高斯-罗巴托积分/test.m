clear

N=80;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x_lobatto=[-1,legendregauss(N,1),1];      %[-1,1]�����õ¸�˹�ް��е�
w_lobatto=zeros(1,N+1);
for k=1:N+1
   w_lobatto(k)=2/N/(N+1)/(legendre(N,0,x_lobatto(k)))^2;           %���õ¸�˹�ް���Ȩ��ϵ��
end

y_lobatto=1./(1+25*x_lobatto.^2);
I_lobatto=y_lobatto*w_lobatto';           %���õ�-��˹-�ް��� ����
error_gauss_lobatto=abs(I_lobatto-2/5*atan(5))

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


x=legendregauss(N+1,0);      %[-1,1]�����õ¸�˹��
w=zeros(1,N+1);
for k=1:N+1
   w(k)=2/((1-x(k)^2)*(legendre(N+1,1,x(k)))^2);           %���õ¸�˹Ȩ��ϵ��
end

y=1./(1+25*x.^2);
I=y*w';                                 %���õ�-��˹ ����
error_gauss=abs(I-2/5*atan(5))
