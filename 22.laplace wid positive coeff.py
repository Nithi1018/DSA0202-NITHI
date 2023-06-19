import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg')

# Define the Laplacian kernel with diagonal extension
kernel = np.array([[0, 1, 0],
                   [1, -8, 1],
                   [0, 1, 0]])

# Apply the Laplacian kernel to the image to obtain the sharpened image
sharpened = cv2.filter2D(image, -1, kernel)

# Display the original and sharpened images
cv2.imshow('Original', image)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
