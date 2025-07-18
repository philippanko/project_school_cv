import cv2

def callback(i): pass

cam = cv2.VideoCapture(0)
while True:
    success, frame = cam.read()

    cv2.imshow("webcam", frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("webcam_r", frame)

    key = cv2.waitKey(50)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
cv2.waitKey(50)