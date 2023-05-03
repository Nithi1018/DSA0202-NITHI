import cv2
import numpy as np

# Load the image and the target points
image = cv2.imread('1.jpg')
target_points = np.array([[0, 0], [500, 0], [500, 500], [0, 500]], dtype=np.float32)

# Set the source points to transform
source_points = np.array([[141, 131], [480, 159], [493, 630], [64, 601]], dtype=np.float32)

# Calculate the homography matrix
homography_matrix, _ = cv2.findHomography(source_points, target_points)

# Perform the transformation
transformed_image = cv2.warpPerspective(image, homography_matrix, (500, 500))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
