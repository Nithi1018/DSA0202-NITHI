import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open video capture device")
    exit()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", width, height)

delay = -34
speed_factor = 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read frame from video capture device")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    cv2.imshow("Video", frame)

    if speed_factor > 1:
        cv2.waitKey(delay * speed_factor)
    elif speed_factor < 1:
        cv2.waitKey(int(delay / speed_factor))
    else:
        cv2.waitKey(delay)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('f'):
        speed_factor = min(speed_factor * 2, 8)
    elif key == ord('s'):

        speed_factor = max(speed_factor / 2, 0.25)

cap.release()
cv2.destroyAllWindows()
