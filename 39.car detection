import cv2

# Load the video file
cap = cv2.VideoCapture('F:/WhatsApp Video 2023-05-11 at 12.12.02.mp4')

# Load the vehicle detection model
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Stop the loop if there are no more frames
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the frame
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected vehicles
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the frame with the vehicle detections
    cv2.imshow('Vehicle Detection', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
