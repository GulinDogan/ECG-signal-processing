import numpy as np
import pandas as pd
import pylab as pl 
import matplotlib.pyplot as plt
from biosppy.signals import ecg
from biosppy.signals import bvp
from biosppy import storage

from sklearn.utils import resample
from keras.utils.np_utils import to_categorical
from sklearn.metrics import confusion_matrix

from train import learning
from vis import my_circle

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

sum = 0
for i in heart_reate_bvp:
    sum += i
avg_heart_rate = sum/len(heart_reate_bvp)

state = []
if 60 < avg_heart_rate < 90:
    state = 0 # normal
else:
    state = 1 # anormal

print("EKG Sinyalinin Durumu: ", state)
print("State type: ", type(state))

pl.plot(heart_rate_ts, heart_reate_bvp, lw=2)
pl.title('Dinlenme Kalp Atım Hızı')
pl.ylabel('Kalp Atım Sayısı')
pl.xlabel('zaman(dakika)')
pl.grid()
pl.show()

new_row = np.append(filtered[0:187], state)
#print("new_row: \n", new_row)

train_df = pd.read_csv("../data/mitbih_train.csv", header=None)
test_df = pd.read_csv("../data/mitbih_test.csv", header=None)

print("train veriseti info:\n",train_df.info())
print("test veriseti info",test_df.info())

train_df[187]=train_df[187].astype(int)
equilibre=train_df[187].value_counts()
print(equilibre)

my_circle(equilibre)

#rint("train_df type: \n",type(train_df))
test_df = np.vstack((test_df, new_row))
#print("test_df type: \n", type(test_df))
test_df =pd.DataFrame(test_df)

learning(train_df,test_df)