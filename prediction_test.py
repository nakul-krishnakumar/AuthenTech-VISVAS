from keras.models import load_model
import preprocessing
import cv2 as cv
import numpy as np

# Load the model
model = load_model("../authentech visvas/signature_verification_model.h5")

# Load images
sig1 = cv.imread("../sign_data/test/049/01_049.png")
sig2 = cv.imread("../sign_data/test/049_forg/01_0114049.PNG")


# Preprocess images
sig1_preprocessed = preprocessing.preprocess(sig1)  # Ensure this outputs a (height, width, channels) array
sig2_preprocessed = preprocessing.preprocess(sig2)

# Resize and expand dimensions if needed
sig1_preprocessed = np.expand_dims(sig1_preprocessed, axis=0)
sig2_preprocessed = np.expand_dims(sig2_preprocessed, axis=0)

# Stack images for Siamese model input
# Check if your model expects [img1, img2] as a list or a numpy array with two images
images_pair = [sig1_preprocessed, sig2_preprocessed]

# Make prediction
prediction = model.predict(images_pair)

print("I'm:", prediction[0][0]*100,"% sure that second image is forged ")
