import cv2
import numpy as np
img = cv2.imread("E:/1.jpg")
roi_points = np.array([(150, 200), (450, 200), (550, 500), (50, 500)])
target_points = np.array([(0, 0), (400, 0), (400, 600), (0, 600)])
M = cv2.getPerspectiveTransform(roi_points.astype(np.float32), target_points.astype(np.float32))
dst = cv2.warpPerspective(img, M, (400, 600))
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
