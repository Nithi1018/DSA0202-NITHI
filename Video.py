import cv2

# Open the video capture device (webcam or file)
cap = cv2.VideoCapture(0)  # change the argument to the path of your video file if needed

# Check if the capture device is open
if not cap.isOpened():
    print("Could not open video capture device")
    exit()

# Get the width and height of the frames
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a window to display the video
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", width, height)

# Loop over the frames of the video
while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Could not read frame from video capture device")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw a rectangle on the frame
    cv2.rectangle(frame, (100, 100), (200, 200), (0, 0, 255), 2)

    # Display the frames
    cv2.imshow("Video", frame)
    cv2.imshow("Grayscale", gray)

    # Wait for a key to be pressed
    key = cv2.waitKey(1)

    # Exit the loop if the 'q' key is pressed
    if key == ord('q'):
        break

# Release the video capture device and destroy the windows
cap.release()
cv2.destroyAllWindows()
