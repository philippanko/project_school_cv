import cv2


import numpy as np


cam = cv2.VideoCapture(0)
while True:
    success, frame = cam.read()
    print(frame.shape)

    cv2.imshow("webcam", frame)

    key = cv2.waitKey(50);

    frame2 = np.zeros(frame.shape)

    for x in range(frame.shape[0]):
        for y in range(frame.shape[1]):
            b, g, r = frame[x, y]
            if r>190 & g < 60 & b < 60:
                frame2[x,y] = [255,255, 255]
    cv2.imshow("red",frame2)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
cv2.waitKey(50);