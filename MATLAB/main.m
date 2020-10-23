clear all
load('ECGraw.mat')

Fs= 1000;
% Values ​​between 1 and 10000 are selected within the signal
index = 1:10000;

ECG = ecg(index);
% R peaks, Heart rate 
% findpeak use to find R peaks
% pk: amplitude, locks: x coordinate
[pks,locs] = findpeaks(ecg(index),...
    'minpeakdistance',100,...
    'MINPEAKHEIGHT',4000);
 
Rpeaks = zeros(1,length(ECG));
Rpeaks(locs) = ECG(locs);

figure
plot(ECG);
hold on
stem(Rpeaks,'r','linewidth',1)

% Calculation of distance with two R peak difference
% Intermediate intervals
RR = diff(locs);
% New figure create and plot
figure
plot(RR, 'ro');



