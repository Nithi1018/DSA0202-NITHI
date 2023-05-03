import cv2
import numpy as np

img = cv2.imread("1.jpg")
M = np.float32([[0.5, 0.5, 50], [0.5, -0.5, 50]])
dst = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
