clc;
close all;
nr_data_bits = 8192;
b_data = (randn(1,nr_data_bits))>0.5; 
%randnn: randomly generates the 8192 elements if the value is greater than 0.5 it will remain true(1) otherwise false(0)
b = (b_data);
d = zeros(1,length(b));
for n=1:length(b)
 if(b(n)==0)
 d(n)=exp(j*2*pi);
 end
 if(b(n)==1)
 d(n)=exp(j*pi);
 end
end
disp(d)
bpsk=d;
%Plotting of BPSK data
figure(1);
plot(d,'o');
axis([-2 2 -2 2])
grid on;
xlabel('real axis');
ylabel('imag axis');
title('BPSK Constellation');
%Addition of Noise 
SNR=0:24;
BER1=[];
SNR1=[];
for SNR = 0:length(SNR)
end
 sigma = sqrt(10.0^(-SNR/10.0));
 snbpsk=(real(bpsk)+sigma.*randn(size(bpsk)))+i.*(imag(bpsk)+sigma*randn(size(bpsk)));
% Plotting of BPSK data with Noise
figure(2);
plot(snbpsk,'o');
axis([-2 2 -2 2]);
grid on;
xlabel('real axis');
ylabel('imag axis');
title('Bpsk constellation with Noise');
 
%Recovering of Data
r = snbpsk;
bhat = (real(r)<0);
bhat(bhat(:));
bhat1 = bhat;
ne = sum(b~=bhat1);
BER = ne/nr_data_bits;
BER1 = [BER1 BER];
SNR1 = [SNR1 SNR];
