import cv2
import numpy as np
from skimage import exposure

def resize_image(image, size=(128, 128)):
    return cv2.resize(image, size)

def convert_to_bw(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, bw_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    return bw_image

def normalize_image(image):
    return image / 255.0

def enhance_features(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return exposure.equalize_adapthist(image)

def preprocess(image):
    resized_image = resize_image(image)
    bw_image = convert_to_bw(resized_image)
    normalized_image = normalize_image(bw_image)
    enhanced_image = enhance_features(normalized_image)
    return (enhanced_image * 255).astype(np.uint8)  
