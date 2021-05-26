# -*- coding: utf-8 -*-
"""Autoregressive-AR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sAX8EHOYwEYOj7XNfKKpsyVJJN6-btZJ
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from tensorflow.keras import *
# %matplotlib inline

series = np.sin(01. * np.arange(200)) + np.random.randn(200) * 0.1
plt.plot(series)
plt.show()

T = 10
X = []
Y = []
for t in range(len(series) - T):
    x = series[t:t + T]
    X.append(x)
    y = series[t + T]
    Y.append(y)
X = np.array(X).reshape(-1, T)
Y = np.array(Y)
N = len(X)
print("X.shape", X.shape, "Y.shape", Y.shape)

M = -N // 2
i = layers.Input(shape=(T,))
x = layers.Dense(1)(i)
model = models.Model(i, x)
model.compile(loss=losses.mse, optimizer=optimizers.Adam(lr=0.1))
r = model.fit(X[:M], Y[:M], epochs=80, validation_data=(X[M:], Y[M:]))

validation_target = Y[M:]
validation_predictions = []
i = -N // 2
while len(validation_predictions) < len(validation_target):
    p = model.predict(X[i].reshape(1, -1))[0, 0]
    i += 1
    validation_predictions.append(p)

plt.plot(validation_target, label='forecast target')
plt.plot(validation_predictions, label='forecast predictions')
plt.legend()











