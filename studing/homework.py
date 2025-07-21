import cv2

cv2.namedWindow('mask')

def callback(i): pass

cv2.createTrackbar('lg','mask',10,255, callback)
cv2.createTrackbar('hg','mask',255,255, callback)
cv2.createTrackbar('lr','mask',10,255, callback)
cv2.createTrackbar('hr','mask',255,255, callback)
cv2.createTrackbar('lb','mask',10,255, callback)
cv2.createTrackbar('hb','mask',255,255, callback)

cam = cv2.VideoCapture(0)

success, last_frame = cam.read()
while True:
    success, frame = cam.read()

    cv2.imshow("webcam", frame)

    last_frame = cv2.addWeighted(last_frame,0.9, frame, 0.1, 0)
    # cv2.imshow("webcam_r", frame[:,:,0])
    # cv2.imshow("webcam_b", frame[:,:,2])
    # cv2.imshow("webcam_g", frame[:,:,1])

    # print(frame[0,0])
    lg = cv2.getTrackbarPos('lg','mask')
    hg = cv2.getTrackbarPos('hg', 'mask')
    lb = cv2.getTrackbarPos('lb','mask')
    hb = cv2.getTrackbarPos('hb', 'mask')
    lr = cv2.getTrackbarPos('lr', 'mask')
    hr = cv2.getTrackbarPos('hr', 'mask')

    mask_diff = cv2.absdiff(last_frame ,frame)

    cv2.imshow('diff', mask_diff)

    mask = cv2.inRange(mask_diff, (lb, lg, lr), (hb, hg, hr))

    cv2.imshow('mask', mask)

    key = cv2.waitKey(50)

    if key == ord('q'):
        break
    if key == ord('u'):
       last_frame = frame

cv2.destroyAllWindows()
cam.release()
cv2.waitKey(50)