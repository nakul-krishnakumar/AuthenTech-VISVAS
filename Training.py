import pandas as pd
import cv2 as cv
import os
import numpy as np
import tensorflow as tf
import Siamese_CNN_Model
from sklearn.metrics import classification_report, confusion_matrix

img_size=(128,128)
print("Creating training dataframe")
training_dataset = pd.read_csv("sign_data/train_data.csv")
file_1s = training_dataset['file1']
file_2s = training_dataset['file2']
image_dir = 'sign_data_processed/train'

# Creating a list of all first images
image_1 = []
for i_path in file_1s:
    image_path = os.path.join(image_dir, i_path)
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if img is not None:  # Check if the image was loaded successfully
        img_resized = cv.resize(img, img_size)  # Resize images to a uniform size
        image_1.append(img_resized.astype('float32') / 255.0)

# Creating a list of all second images
image_2 = []
for i_path in file_2s:
    image_path = os.path.join(image_dir, i_path)
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if img is not None:  # Check if the image was loaded successfully
        img_resized = cv.resize(img, img_size)  # Resize images to a uniform size
        image_2.append(img_resized.astype('float32') / 255.0)

labels = training_dataset['forged'].values  # Ensure labels are a NumPy array

# Creating a training DataFrame
training_dataframe = pd.DataFrame({
    'image1': image_1,
    'image2': image_2,
    'label': labels
})

print("Training DataFrame created successfully!")
print("Creating testing DataFrame")

# Process the testing dataset
testing_dataset = pd.read_csv("sign_data/test_data.csv")
file_1s = testing_dataset['file1']
file_2s = testing_dataset['file2']
image_dir = 'sign_data_processed/test'

# Creating a list of all first images for testing
test_image_1 = []
for i_path in file_1s:
    image_path = os.path.join(image_dir, i_path)
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if img is not None:  # Check if the image was loaded successfully
        img_resized = cv.resize(img, img_size)  # Resize images to a uniform size
        test_image_1.append(img_resized.astype('float32') / 255.0)

# Creating a list of all second images for testing
test_image_2 = []
for i_path in file_2s:
    image_path = os.path.join(image_dir, i_path)
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if img is not None:  # Check if the image was loaded successfully
        img_resized = cv.resize(img, img_size)  # Resize images to a uniform size
        test_image_2.append(img_resized.astype('float32') / 255.0)

test_labels = testing_dataset['forged'].values  # Ensure test labels are a NumPy array

# Creating a testing DataFrame
testing_dataframe = pd.DataFrame({
    'image1': test_image_1,
    'image2': test_image_2,
    'label': test_labels
})

print("Testing DataFrame Created Successfully!")

# Creating the model using the Siamese_CNN_model module
model = Siamese_CNN_Model.create_Siamese_CNN_model()

# Convert lists of images to 4D NumPy arrays
img1 = tf.convert_to_tensor(np.array(image_1), dtype=tf.float32)
img2 = tf.convert_to_tensor(np.array(image_2), dtype=tf.float32)
train_labels = tf.convert_to_tensor(labels, dtype=tf.float32)  # Ensure labels are float32

# Fit the model
model.fit([img1, img2], 
          train_labels, 
          batch_size=10, epochs=20)

# Making predictions
predictions = model.predict([tf.convert_to_tensor(np.array(test_image_1), dtype=tf.float32), 
                              tf.convert_to_tensor(np.array(test_image_2), dtype=tf.float32)])
predictions = (predictions > 0.5).astype(int)  # Convert probabilities to binary predictions

# Evaluate model performance
print("Evaluating model performance")
print(confusion_matrix(test_labels, predictions))
print(classification_report(test_labels, predictions))
