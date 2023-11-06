clc;
m=0;
sd=1;
x=-6:0.1:6;
y=normpdf(x,m,sd);
plot(x,y);
axis([-6 6 0 1]); %range from -6 to 6 and y-axis ranges from 0 to 1.
title("CASE-1: mean=0,std dev=1");
xlabel("x values--- >");
ylabel("PDF----->");
subplot(3,2,1);
plot(x,y)
grid on;
m=1;
sd=1;
x1=-6:0.1:6;
y1=normpdf(x1,m,sd);
plot(x1,y1);
axis([-6 6 0 1]); %range from -6 to 6 and y-axis ranges from 0 to 1.
title("CASE-1: mean=1,std dev=1");
xlabel("x values--- >");
ylabel("PDF----->");
subplot(3,2,2);
plot(x1,y1)
grid on;
m=-1;
sd=1;
x2=-6:0.1:6;
y2=normpdf(x2,m,sd);
plot(x2,y2);
axis([-6 6 0 1]); %range from -6 to 6 and y-axis ranges from 0 to 1.
title("CASE-1: mean=0,std dev=1");
xlabel("x values--- >");
ylabel("PDF----->");
subplot(3,2,3);
plot(x2,y2)
grid on;
m=0;
sd=1.5;
x3=-6:0.1:6;
y3=normpdf(x3,m,sd);
plot(x3,y3);
axis([-6 6 0 1]); %range from -6 to 6 and y-axis ranges from 0 to 1.
title("CASE-1: mean=0,std dev=1");
xlabel("x values--- >");
ylabel("PDF----->");
subplot(3,2,4);
plot(x3,y3)
grid on;
m=0;
sd=0.5;
x4=-6:0.1:6;
y4=normpdf(x4,m,sd);
plot(x4,y4);
axis([-6 6 0 1]); %range from -6 to 6 and y-axis ranges from 0 to 1.
title("CASE-1: mean=0,std dev=1");
xlabel("x values--- >");
ylabel("PDF----->");
subplot(3,2,5);
plot(x4,y4)
grid on;
m=1;
sd=0.5;
x5=-6:0.1:6;
y5=normpdf(x5,m,sd);
plot(x5,y5);
axis([-6 6 0 1]); %range from -6 to 6 and y-axis ranges from 0 to 1.
title("CASE-1: mean=0,std dev=1");
xlabel("x values--- >");
ylabel("PDF----->");
subplot(3,2,6);
plot(x5,y5)
grid on;
