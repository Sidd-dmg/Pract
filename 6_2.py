% Write program to calculate and plot PSD and Autocorrelation of a Gaussian
% (Normal) Process
n=1000;
mu=2; %define mean
sigma=4; %define std deviation
y=normrnd(mu,sigma,1,n);
Gy=periodogram(y); %Calculation of PSD
Ry=abs(ifft(Gy,256));
Ry=[Ry(130:256)' Ry(1:129)']
t=-127:1:128;
figure
subplot(1,2,1)
plot(Gy)
xlabel("Frequencysamples");
title("PSD")
subplot(1,2,2)
stem(t,Ry)
xlabel("time shift")
ylabel("autocorrelation")
