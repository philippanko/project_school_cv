import cv2
import numpy as np

bpm = 120;

cam = cv2.VideoCapture(0)
while(True):
    success, frame = cam.read()
    print(frame[100,200,1])

    # frame[100 : 300, 200:500, 0] +=100


    shift = np.random.randint(30)+10


    cv2.imshow("webcam", frame)

    key = cv2.waitKey(50);

    if(key == ord('q')):
        break

cv2.destroyAllWindows()
cam.release()
cv2.waitKey(50);