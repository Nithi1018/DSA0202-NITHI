import cv2

# Load the image
img = cv2.imread("E:/1.jpg")

# Load the watermark image
watermark = cv2.imread("E:/1.jpg", cv2.IMREAD_UNCHANGED)

# Resize the watermark to match the size of the original image
watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))

# Merge the watermark with the original image
result = cv2.addWeighted(img, 1, watermark, 0.3, 0)

# Save the result
cv2.imwrite('path/to/result.jpg', result)
