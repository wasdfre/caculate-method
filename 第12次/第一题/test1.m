clear


N=5000;
b=rand(N,1);             %�����������F

A=zeros(N);
a0=rand(N,1);
for k=0:N-1
   A(:,k+1)=circshift(a0,k);        %�������ѭ������D
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
time0=cputime;

x_inv=inv(A)*b;             %ֱ���������



time1=cputime;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


x_gauss=A\b;             %��˹��ȥ������

% [L,U,P]=lu(A);
% x_PLU=U\(L\(P*b));             %PLU�ֽ����


time2=cputime;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


x_fft=ifft(diag(1./fft(A(:,1)))*fft(b));         %���ÿ��ٸ���Ҷ�任����

time3=cputime;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

error=norm(x_inv-x_fft)+norm(x_gauss-x_fft);         %�������
time_inv=time1-time0;
time_gauss=time2-time1;
time_fft=time3-time2;

fprintf('ֱ���������CPUʱ��Ϊ%f\n', time_inv);
fprintf('��˹��ȥ������CPUʱ��Ϊ%f\n', time_gauss);
fprintf('FFT����CPUʱ��Ϊ%f\n', time_fft);

error
