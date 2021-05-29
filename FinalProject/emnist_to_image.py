from PIL import Image
import numpy as np
#imports
from __future__ import print_function
import pandas as pd
import os

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.utils import np_utils
from sklearn.model_selection import train_test_split

train = pd.read_csv(r'C:\Users\mohan\Desktop\FinalProject\emnist-bymerge-train.csv')
test = pd.read_csv(r'C:\Users\mohan\Desktop\FinalProject\emnist-bymerge-test.csv')

#declarations
batch_size = 200
num_classes = 47
epochs = 12
img_rows, img_cols = 28, 28

y_train = train.iloc[:,0]
x_train = train.iloc[:,1:]
y_test = test.iloc[:,0]
x_test = test.iloc[:,1:]

#Converting the image data format to a 2D matrix
if K.image_data_format() == 'channels_first':
    x_train = x_train.values.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.values.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.values.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.values.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
    
#Further reshaping and converting values from 0-255 to 0-1
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

#categorizing the data into binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

for i in range(1000):
    temp = x_train[i]
    temp=np.reshape(temp,(28,28))
    temp=temp*255
    im = Image.fromarray(temp).convert('L')
    im.save(r'C:\Users\mohan\Desktop\FinalProject\emnist'+str(i)+'.png')