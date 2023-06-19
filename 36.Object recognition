import cv2

# Load the image
img = cv2.imread('watch.jpg')

# Load the model
model = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

# Set the input image and scale factor
input_blob = cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False)
model.setInput(input_blob)

# Run the detection and get the output
output = model.forward()

# Loop through the detected objects and draw rectangles around the watches
for detection in output[0,0,:,:]:
    confidence = detection[2]
    if confidence > 0.5:
        left = int(detection[3] * img.shape[1])
        top = int(detection[4] * img.shape[0])
        right = int(detection[5] * img.shape[1])
        bottom = int(detection[6] * img.shape[0])
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)

# Display the image with detections
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
