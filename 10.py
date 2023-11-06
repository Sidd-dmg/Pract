clc;
close all; 
n=6;
k=3;
p=[0 1 1;1 0 1;1 1 0];
%parity matrix
d=input("Enter three bit message :");
ik=eye(k);
g=cat(2,ik,p);
%concatenation
disp("Generator matrix :");
disp(g);
c1=mtimes(d,g); 
c=mod(c1,2);
%remainder is output
disp("The codeword for given mesage is :"); 
disp(c);
