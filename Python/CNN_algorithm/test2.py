import numpy as np 
import pandas as pd 
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Activation

import pylab as pl 
from biosppy.signals import ecg

mit_train_data = pd.read_csv("../data/mitbih_train.csv", header=None)
mit_test_data = pd.read_csv("../data/mitbih_test.csv", header=None)

# Separate features and targets
print("--- X ---")
X = mit_train_data.loc[:, mit_train_data.columns != 187]
print(X.head())
print(X.info())

print("--- Y ---")
y = mit_train_data.loc[:, mit_train_data.columns == 187]
y = to_categorical(y)


print("--- testX ---")
testX = mit_test_data.loc[:, mit_test_data.columns != 187]
print(testX.head())
print(testX.info())

print("--- testy ---")
testy = mit_test_data.loc[:, mit_test_data.columns == 187]
testy = to_categorical(testy)

#######################

N = len(X[0])  # number of samples
T = (N - 1) / 1000  # duration
ts = np.linspace(0, T, N, endpoint=False)  # relative timestamps

output = ecg.ecg(signal=X[0], show=False)
ts = output[0]

# Filitrelenen sinyal 
filtered = output[1]
pl.plot(ts, filtered)
pl.title('Filitreli ECG Signal')
pl.ylabel('Genlik')
pl.xlabel('zaman(saniye)')
pl.grid()
pl.show()


# define model 
model = Sequential()

model.add(Dense(50, activation='relu', input_shape=(187,)))
model.add(Dense(50, activation='relu'))
model.add(Dense(5, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X, y, epochs=100)

print("Evaluation: ")
mse, acc = model.evaluate(testX, testy)
print('mean_squared_error :', mse)
print('accuracy:', acc)