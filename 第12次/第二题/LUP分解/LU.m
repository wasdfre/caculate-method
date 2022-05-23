function [L,U] =LU(A)
    N=size(A,1);
    L=zeros(N,N);
    U=zeros(N,N);
    for k =1:N
        L(k,k)=1;
        %先算u
        for j =1:N
            if(k==1)
                U(k,j)=A(k,j);
     
            else
                U(k,j)=A(k,j)-L(k,1:k-1)*U(1:k-1,j);
            end
        end
        %再算l
        for i =k+1:N
            if(k==1)
                L(i,k)=A(i,k)/U(k,k);
            else
                L(i,k)=((A(i,k)-L(i,1:k)*U(1:k,k))./U(k,k));
    
            end        
        end
    end
end


function x= downtri(A,Y)
    m=A.shape(0);
    x=zeros(m);
    for k =1:m
        x(k)=(Y(k)-dot(A(k,0:k),x(0:k)))/A(k,k);
    end
end
function x= uptri(A,Y)
    m=A.shape(0);
    x=np.zeros(m);
    for k =1:m
        x(m-k+1)=(Y(m-k+1)-dot(A(m-k+1,m-k+2:m),x(m-k+2:m)))/A(m-k+1,m-k+1);
    end
end

