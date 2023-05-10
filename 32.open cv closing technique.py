import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread("E:/1.jpg", cv2.IMREAD_GRAYSCALE)

# Define kernel size and shape for closing operation
kernel = np.ones((5,5), np.uint8)

# Perform closing operation on image
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display original image and result of closing operation
cv2.imshow('Original', img)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
