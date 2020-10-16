clear all
load('ECGraw.mat')

Fs= 1000;
% Sinyal i�inden 1 ve 10000 aras?ndaki de?erleri alaca??z
index = 1:10000;

ECG = ecg(index);
% R  tepeleri, en y�ksek tepeler kalp at?m? 
% ollarak da de?erlendirilebilir
% R tepeleri yakalamak i�in findpeak kullan?labilir.
%pk: Genlik, locks: x koor
[pks,locs] = findpeaks(ecg(index),...
    'minpeakdistance',100,...
    'MINPEAKHEIGHT',4000);
 
Rpeaks = zeros(1,length(ECG));
Rpeaks(locs) = ECG(locs);

figure
plot(ECG);
hold on
stem(Rpeaks,'r','linewidth',1)

% iki ar tepesinin fark?n? alarak mesafeyi �l��yoruz.
% Bunlar: Ara intervaller
RR = diff(locs);
% New figure create and plot
figure
plot(RR, 'ro');



