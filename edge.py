import cv2
import numpy as np
img = cv2.imread("1.jpg")
edges = cv2.Canny(img, 100, 200)
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
