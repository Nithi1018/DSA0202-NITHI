import cv2
import numpy as np

# Load the images
img1 = cv2.imread("E:/1.jpg")
img2 = cv2.imread("E:/1.jpg")

# Define the ROI
x, y, w, h = 100, 100, 200, 200
roi = img1[y:y+h, x:x+w]

# Resize the ROI
roi_resized = cv2.resize(roi, (w, h))

# Create a mask
img2gray = cv2.cvtColor(roi_resized,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Paste the ROI onto the second image
img2_bg = cv2.bitwise_and(img2,img2,mask = mask_inv)
img1_fg = cv2.bitwise_and(roi_resized,roi_resized,mask = mask)
dst = cv2.add(img2_bg,img1_fg)
img2[y:y+h, x:x+w] = dst

# Display the result
cv2.imshow('Result', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

