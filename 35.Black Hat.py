import cv2
import numpy as np

# Read in an image
img = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg', 0)

# Define a kernel
kernel = np.ones((5,5), np.uint8)

# Perform the blackhat operation
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display the original and blackhat-processed images
cv2.imshow('Original', img)
cv2.imshow('Blackhat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
