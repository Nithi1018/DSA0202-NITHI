import cv2

# Load the image
img = cv2.imread('E:/1.jpg', 0)

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
