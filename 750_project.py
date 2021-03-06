# -*- coding: utf-8 -*-
"""750 Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P70OUJyVgdOJAnpyueeA-q3Oe6HWyMpn
"""

import keras
from keras.utils.np_utils import to_categorical
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras import backend as k
import numpy as np
import time

(X_train, y_train), (X_test, y_test) = mnist.load_data()

def print_time(s, secs):
  minutes = int(secs / 60)
  seconds = secs - minutes * 60
  print("{}:".format(s))
  print("{m}m {s}s".format(m=minutes,s=seconds))

img_rows, img_cols=28, 28

X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

build_model_start = time.time()
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
#model.add(Conv2D(64, (3, 3), activation='relu'))
#model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

build_model_finish = time.time()

batch_size = 1024
num_epoch = 5
train_model_start = time.time()
model_log = model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=num_epoch,
          verbose=1,
          validation_data=(X_test, y_test))
train_model_finish = time.time()

test_model_start = time.time()
score = model.evaluate(X_test, y_test, verbose=0)
print('loss=', score[0])
print('accuracy=', score[1])
test_model_finish = time.time()

build_time = build_model_finish - build_model_start
print_time("Build Time", build_time)

train_time = train_model_finish - train_model_start
print_time("Train Time", train_time)

test_time = test_model_finish - test_model_start
print_time("Test Time", test_time)
