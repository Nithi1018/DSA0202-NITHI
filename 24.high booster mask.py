import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg', cv2.IMREAD_GRAYSCALE)

# Apply a Gaussian filter to the image
blur = cv2.GaussianBlur(img, (5,5), 0)

# Calculate the high-pass filter
high_pass = img - blur

# Define the constant A for sharpening
A = 2.0

# Multiply the high-pass filter by the constant A
high_boost = A * high_pass

# Add the high-pass filter to the original image
sharpened = img + high_boost

# Display the original and sharpened images
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
