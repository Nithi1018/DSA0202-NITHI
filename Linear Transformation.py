import cv2
import numpy as np

image = cv2.imread('E:/1.jpg')
source_points = np.array([[141, 131], [480, 159], [493, 630], [64, 601]], dtype=np.float32)
target_points = np.array([[0, 0], [500, 0], [500, 500], [0, 500]], dtype=np.float32)

num_points = source_points.shape[0]
A = np.zeros((2*num_points, 9), dtype=np.float64)
for i in range(num_points):
    x, y = source_points[i]
    u, v = target_points[i]
    A[2*i] = [x, y, 1, 0, 0, 0, -u*x, -u*y, -u]
    A[2*i+1] = [0, 0, 0, x, y, 1, -v*x, -v*y, -v]

_, _, V = np.linalg.svd(A)
h = V[-1, :]
homography_matrix = h.reshape((3, 3))

transformed_image = cv2.warpPerspective(image, homography_matrix, (500, 500))

cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
