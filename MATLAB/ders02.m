
% Sürekeli zamanda grafik
t = 0:0.01:12;
xt = sin(pi/3*t);
figure,plot(t, xt); % t zaman?na bagl? xt sinyalii
xlabel('X lablel name');
s = size(xt);
l = length(xt);

% Ayr?k zamanl?
n = 0:12;
xn = sin(pi/3*n);
figure,stem(n,xn)
% ayr?k zamanl? sinyal ile sürekli zamanl? sinyali 
% çak??t?rd???m?zda kes?ti?i noktalar? gösterdim.
figure,stem(n,xn); hold on; plot(t,xt);

% iki ayr?k zamanl? sinyalin toplanmas? 
n2 = -3:3;
x1 = [1 2 3 0 -2 -2 -1];
x2 = [-3 -1 -3 1 2 3 3];
x3 = x1+x2;
figure,stem(n2,x1);
figure,stem(n2,x2);
figure,stem(n2,x3);