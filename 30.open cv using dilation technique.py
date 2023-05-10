import cv2
import numpy as np

# Read in the image
img = cv2.imread("E:/1.jpg")

# Create a structuring element for dilation
kernel = np.ones((5,5),np.uint8)

# Perform dilation
dilation = cv2.dilate(img,kernel,iterations = 1)

# Display the original and the dilated image side by side
cv2.imshow('Original', img)
cv2.imshow('Dilated', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
