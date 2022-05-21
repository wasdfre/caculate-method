clear


N=5000;
b=rand(N,1);             %随机生成向量F

A=zeros(N);
a0=rand(N,1);
for k=0:N-1
   A(:,k+1)=circshift(a0,k);        %随机生成循环矩阵D
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
time0=cputime;

x_inv=inv(A)*b;             %直接求逆计算



time1=cputime;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


x_gauss=A\b;             %高斯消去法计算

% [L,U,P]=lu(A);
% x_PLU=U\(L\(P*b));             %PLU分解计算


time2=cputime;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


x_fft=ifft(diag(1./fft(A(:,1)))*fft(b));         %利用快速傅里叶变换计算

time3=cputime;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

error=norm(x_inv-x_fft)+norm(x_gauss-x_fft);         %检验误差
time_inv=time1-time0;
time_gauss=time2-time1;
time_fft=time3-time2;

fprintf('直接求逆计算CPU时间为%f\n', time_inv);
fprintf('高斯消去法计算CPU时间为%f\n', time_gauss);
fprintf('FFT计算CPU时间为%f\n', time_fft);

error
