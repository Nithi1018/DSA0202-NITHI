import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg', cv2.IMREAD_GRAYSCALE)

# Create the Laplacian filter with a negative center coefficient
laplacian_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Apply the Laplacian filter to the image
sharpened = cv2.filter2D(img, -1, laplacian_filter)

# Add the sharpened image to the original image
sharpened_img = cv2.addWeighted(img, 1.5, sharpened, -0.5, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
