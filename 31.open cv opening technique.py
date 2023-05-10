import cv2
import numpy as np

# Read in the image
img = cv2.imread("E:/1.jpg")

# Create a structuring element for opening
kernel = np.ones((5,5),np.uint8)

# Perform opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Display the original and the opened image side by side
cv2.imshow('Original', img)
cv2.imshow('Opened', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
