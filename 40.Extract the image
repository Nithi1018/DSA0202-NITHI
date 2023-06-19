import cv2
img = cv2.imread('1.jpg')
start_point = (50, 50)
end_point = (200, 200)
color = (0, 0, 255)
thickness = 2
rect_img = cv2.rectangle(img, start_point, end_point, color, thickness)
cv2.imshow('Image with Rectangle', rect_img)
cv2.waitKey(0)
obj_img = img[start_point[1]:end_point[1], start_point[0]:end_point[0]]
cv2.imshow('Extracted Object', obj_img)
cv2.waitKey(0)
cv2.imwrite('object.jpg', obj_img)
cv2.destroyAllWindows()
