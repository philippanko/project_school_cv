import cv2

cam = cv2.VideoCapture(0)
while(True):
    success, frame = cam.read()
    print(frame[100,200,1])

    cv2.imshow("webcam", frame)

    key = cv2.waitKey(50);

    if(key == ord('q')):
        break

cv2.destroyAllWindows()
cam.release()
cv2.waitKey(50);