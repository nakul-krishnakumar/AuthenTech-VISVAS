import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, Dense, ReLU, MaxPooling2D, Flatten, Lambda, Input
from keras import Model

def CNN_base():
   model=Sequential([
      Conv2D(64, (10,10),activation='relu',input_shape=(128,128,1)),
      MaxPooling2D(),
      Conv2D(128, (7, 7), activation='relu'),
      MaxPooling2D(),
      Conv2D(128, (4, 4), activation='relu'),
      MaxPooling2D(),
      Conv2D(256, (4, 4), activation='relu'),
      MaxPooling2D(),
      Conv2D(256, (4, 4), activation='relu'),
      Flatten(),
      Dense(4096, activation='sigmoid')
   ])
   return model

def Siamese_CNN():
   base_CNN_body=CNN_base()
   
   #DEFINING INPUT LAYERS
   original_image = Input(shape=(128,128,1))
   train_test_image = Input(shape=(128,128,1))
   
   processed_1 = base_CNN_body(original_image)
   processed_2 = base_CNN_body(train_test_image)

   distance = Lambda(lambda tensors: tf.abs( tensors[0] - tensors[1] ) )  ([processed_1, processed_2])
   output = Dense(1, activation='sigmoid')(distance)
   model = Model(inputs=[original_image, train_test_image], outputs=output)
   return model

def create_Siamese_CNN_model():
   model=Siamese_CNN()
   model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
   return model


