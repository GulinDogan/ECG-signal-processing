import numpy as np
import pylab as pl 
from biosppy.signals import ecg
from biosppy.signals import bvp
from biosppy import storage

# load raw ECG signal
signal, mdata = storage.load_txt('../data/ecg.txt')
Fs = mdata['sampling_rate']
N = len(signal)  # number of samples
T = (N - 1) / Fs  # duration
ts = np.linspace(0, T, N, endpoint=False)  # relative timestamps
pl.plot(ts, signal, lw=2)
pl.title('EKG Sinyali')
pl.ylabel('Genlik')
pl.xlabel('zaman(saniye)')
pl.grid()
pl.show()

out = ecg.ecg(signal=signal, sampling_rate=Fs, show=False)

# Filitrelenen sinyal 
filtered = out[1]
pl.plot(ts, filtered, lw=2)
pl.title('Filitreli ECG Signal')
pl.ylabel('Genlik')
pl.xlabel('zaman(saniye)')
pl.grid()
pl.show()

Rpeaks_x = out[2]
Rpeaks_x = Rpeaks_x*0.001
# print(type(Rpeaks_x))

print("R-R mesafe :\n",  np.diff(Rpeaks_x))  

heart_rate_ts = out[5]
# print("kalp atımının ölçüm zaman aralıkları (dakika): \n", +heart_rate_ts)
heart_reate_bvp = out[6]
print("Dinlenme kalp atım hızı:\n", +heart_reate_bvp)

pl.plot(heart_rate_ts, heart_reate_bvp, lw=2)
pl.title('Dinlenme Kalp Atım Hızı')
pl.ylabel('Kalp Atım Sayısı')
pl.xlabel('zaman(dakika)')
pl.grid()
pl.show()
