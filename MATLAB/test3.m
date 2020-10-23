% call dirack function, x=0, y=1 
[dirac1, xn] = diracFunction(-30,10,0);
x = dirac1;
figure,stem(xn,x);

[dirac2, nx] = diracFunction(-5,5,0);
[dirac3, nx] = diracFunction(-5,5,1);
[dirac4, nx] = diracFunction(-5,5,2);

xn = 3*dirac2-5*dirac3+6*dirac4;

figure,stem (nx, dirac3, 'filled', 'LineWidth', 4);
figure,stem (nx, xn, 'filled', 'LineWidth', 4);