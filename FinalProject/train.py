#imports
from __future__ import print_function
import numpy as np
import pandas as pd

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

def rotate(img):
   # Used to rotate images (for some reason they are transposed on read-in)
   flipped = np.fliplr(img)
   return np.rot90(flipped)

train = pd.read_csv("emnist-bymerge-train.csv")
test = pd.read_csv("emnist-bymerge-test.csv")

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

for i in range(len(x_train)):
    x_train[i] = rotate(x_train[i])
    
for i in range(len(x_test)):
    x_test[i] = rotate(x_test[i])



#building the model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])


#training the model
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])




#saving the model

#saving architecture
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

#saving weights
model.save_weights("model.h5")
print("Saved model to disk")
