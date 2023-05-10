import cv2
import numpy as np

# Read in the image
img = cv2.imread("E:/1.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element for erosion
kernel = np.ones((5, 5), np.uint8)

# Apply the erosion operation
eroded_img = cv2.erode(img, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
