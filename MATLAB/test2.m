
% Graphics in continuous time
t = 0:0.01:12;
xt = sin(pi/3*t);
figure,plot(t, xt); % t depends on xt signal
xlabel('X lablel name');
s = size(xt);
l = length(xt);

% Discrete time signal
n = 0:12;
xn = sin(pi/3*n);
figure,stem(n,xn)
% Display of breakpoints when 
% the discrete time signal and continuous time signal overlap
figure,stem(n,xn); hold on; plot(t,xt);

% Add two discrete time signal 
n2 = -3:3;
x1 = [1 2 3 0 -2 -2 -1];
x2 = [-3 -1 -3 1 2 3 3];
x3 = x1+x2;
figure,stem(n2,x1);
figure,stem(n2,x2);
figure,stem(n2,x3);