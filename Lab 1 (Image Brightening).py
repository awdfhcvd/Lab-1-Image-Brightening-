import cv2
import numpy as np
imagedata_brt = cv2.imread('IMG_2828.jpg')
cv2.imshow("Original", imagedata_brt)
Intensity_Matrix = np.ones(imagedata_brt.shape, dtype = "uint8") * 75
print(Intensity_Matrix)
brightened_image = cv2.add(imagedata_brt, Intensity_Matrix)
cv2.imshow("Bright", brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
