import cv2
import numpy as np

# Load the input image
img = cv2.imread("E:/1.jpg")

# Define the sharpening filter
kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

# Apply the filter to the image using the cv2.filter2D() function
sharpened_img = cv2.filter2D(img, -1, kernel)

# Display the input and sharpened images
cv2.imshow('Input Image', img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
