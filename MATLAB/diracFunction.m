function [dirac,nx] = diracFunction(nba,nbi,n0)
% nba:  x ekseninde ba?lang?ç
% nbi: x eksenindde biti?
% n0: kayd?rma miktar?

nx = nba:nbi;
dirac = (nx == n0);

end

