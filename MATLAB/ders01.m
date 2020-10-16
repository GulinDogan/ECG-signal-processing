
t = -4*pi:0.01:4*pi;

x1 = 100*sin(2*pi*t);  

x3 = 50*sin(2*pi*3*t);

x5 = 35*sin(2*pi*5*t);

gurultu = 100*rand(1, length(x1));

toplamIsaret = (x1+x3+x5+gurultu);

plot(t, toplamIsaret, 'linewidth', 3);