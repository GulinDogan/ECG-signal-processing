import numpy as np 
import pandas as pd 
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Activation

import pylab as pl 
from biosppy.signals import ecg

def learning(train_df,test_df):

    # Separate features and targets
    print("--- X ---")
    X = train_df.loc[:, train_df.columns != 187]
    print(X.head())
    print(X.info())

    print("--- Y ---")
    y = train_df.loc[:, train_df.columns == 187]
    y = to_categorical(y)
    print("train y:\n", y)

    print("--- testX ---")
    testX = test_df.loc[:, test_df.columns != 187]
    print(testX.head())
    print(testX.info())

    print("--- testy ---")
    testy = test_df.loc[:, test_df.columns == 187]
    testy = to_categorical(testy)
    print("testy:\n", testy)

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