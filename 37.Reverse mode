import cv2

# Open the video file
cap = cv2.VideoCapture('video.mp4')

# Get the total number of frames in the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop through the frames in reverse order and display them
for i in reversed(range(num_frames)):
    # Set the current frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    
    # Read the frame
    ret, frame = cap.read()
    
    # Display the frame
    cv2.imshow('Reverse Video', frame)
    
    # Check for user input to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
