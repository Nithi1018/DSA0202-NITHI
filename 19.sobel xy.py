import cv2
import numpy as np

# Load image in grayscale mode
img = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter in X direction
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter in Y direction
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine the results of the Sobel filters
sobel_combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Display the result
cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
