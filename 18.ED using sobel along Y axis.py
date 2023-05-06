import cv2
import numpy as np

# Load the image
img = cv2.imread('E:/1.jpg', 0)

# Apply Sobel filter along the Y-axis
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert the output to absolute values
sobely = np.abs(sobely)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Edge Detection (Y-axis)', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
