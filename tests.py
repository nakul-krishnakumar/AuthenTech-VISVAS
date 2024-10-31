import Preprocess
import cv2 as cv

'''-------------------------------TESTING PREPROCESS MODULE-------------------------------'''

def test_preprocess_module(image, height,width):
   image_resized=Preprocess.resize_image(image,height,width)
   image_BW=Preprocess.convert_to_bw(image)
   image_normalized=Preprocess.normalize_image(image)
   image_enhanced=Preprocess.enhance_features(image)
   image_preprocessed=Preprocess.preprocess(image, height,width)
   cv.imshow("image resized",image_resized )
   cv.waitKey(0)
   cv.imshow("image B&W",image_BW)
   cv.waitKey(0)
   cv.imshow("image normalized",image_normalized )
   cv.waitKey(0)
   cv.imshow("image enhanced",image_enhanced )
   cv.waitKey(0)
   cv.imshow("image preprocessed",image_preprocessed )
   print(image_preprocessed)
   cv.waitKey(0)

image=cv.imread(r'sign_data/train/001/001_01.PNG')

'''--tests--'''
test_preprocess_module(image,256,256)
print(image)