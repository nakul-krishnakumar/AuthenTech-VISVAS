import preprocessing
import cv2 as cv

'''-------------------------------TESTING PREPROCESS MODULE-------------------------------'''

def test_preprocess_module(image, height, width):
    if image is None:
        print("Error: Image could not be loaded. Please check the file path and extension.")
        return
    
    # Testing different preprocessing steps
    image_resized = preprocessing.resize_image(image, height, width)
    image_BW = preprocessing.convert_to_bw(image)
    image_normalized = preprocessing.normalize_image(image)
    image_enhanced = preprocessing.enhance_features(image)
    image_preprocessed = preprocessing.preprocess(image, height, width)
    
    # Display results
    cv.imshow("Image Resized", image_resized)
    cv.waitKey(0)
    cv.imshow("Image B&W", image_BW)
    cv.waitKey(0)
    cv.imshow("Image Normalized", image_normalized)
    cv.waitKey(0)
    cv.imshow("Image Enhanced", image_enhanced)
    cv.waitKey(0)
    cv.imshow("Image Preprocessed", image_preprocessed)
    print("Preprocessed Image Array:", image_preprocessed)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Provide a complete image path with an extension
image = cv.imread('sign_data/train/001/001_01.png')

'''--tests--'''
test_preprocess_module(image, 256, 256)
print("Original Image Array:", image)
