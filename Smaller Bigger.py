import cv2

img = cv2.imread("1.jpg")
height, width = img.shape[:2]

scale_factor = 1.5
bigger_img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))

scale_factor = 0.5
smaller_img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))

cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger_img)
cv2.imshow("Smaller Image", smaller_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
