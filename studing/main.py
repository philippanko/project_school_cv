import cv2

cv2.namedWindow('mask')

def callback(i): pass

cv2.createTrackbar('lg','mask',0,255, callback)
cv2.createTrackbar('hg','mask',255,255, callback)

cam = cv2.VideoCapture(0)
while True:
    success, frame = cam.read()

    cv2.imshow("webcam", frame)
    # cv2.imshow("webcam_r", frame[:,:,0])
    # cv2.imshow("webcam_b", frame[:,:,2])
    # cv2.imshow("webcam_g", frame[:,:,1])

    # print(frame[0,0])
    lg = cv2.getTrackbarPos('lg','mask')
    hg = cv2.getTrackbarPos('hg', 'mask')

    mask = cv2.inRange(frame, (0, lg, 0), (255, hg, 255))

    cv2.imshow('mask', mask)

    key = cv2.waitKey(50)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
cv2.waitKey(50)