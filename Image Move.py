import cv2
img = cv2.imread("E:/1.jpg")
x, y = 100, 100
dx, dy = 50, 50
def move_image():
    global x, y, dx, dy
    x += dx
    y += dy
    if x < 0 or x > img.shape[1] or y < 0 or y > img.shape[0]:
        dx = -dx
        dy = -dy
def draw_image():
    global x, y
    cv2.imshow("Moving Image", img)
    cv2.moveWindow("Moving Image", x, y)
draw_image()
while True:
    move_image()
    draw_image()
    key = cv2.waitKey(50)
    if key != -1:
        break
cv2.destroyAllWindows()
