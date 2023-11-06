%Simulation study of various Entropies and Mutual Information in a
%communication system clc;
clear all;
close all;
i=input("Enter no. of elements:");
p=input("Enter probability:");
q=input("Enter conditional probability matrix:");
sum=0;
%entropy H(x) 
for n=1:i
H=sum+(p(n)*log2(1/p(n))); 
sum=H;
end 
disp("H(x):"); 
disp(H);


%Joint Probabilty Matrix 
for n=1:i
for m=1:i
a(n,m)=q(n,m)*p(n);
end
end
disp("P(X,Y):");
disp(a);


%entropy H(Y/X) 
d=0
for n=1:i
for m=1:i
H1=d+(a(n,m)*log2(1/q(n,m))); 
d=H1;
end
end
disp("H(Y/X):"); 
disp(H1);


%probability P(Y) 
for n=1:i
w=0;
for m=1:i
s(n)=w+a(m,n); 
w=s(n);
end
end
 
disp("P(Y/X):"); 
disp(s);


%entropy H(Y) k=0;
for n=1:i;
H2=k+(s(n)*log2(1/s(n))); 
k=H2;
end
disp("H(Y):");
disp(H2);

%Find Mutual Information m=H2-H1;
disp("MI="); 
disp(m);
