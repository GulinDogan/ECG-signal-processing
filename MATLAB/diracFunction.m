function [dirac,nx] = diracFunction(nba,nbi,n0)
% nba:  origin of the x-axis
% nbi: end of the x-axis
% n0: shift amounta

nx = nba:nbi;
dirac = (nx == n0);

end

