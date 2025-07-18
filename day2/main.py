import cv2

cam = cv2.VideoCapture(0)
while True:
    try:
        success, frame = cam.read()

        cv2.imshow("webcam", frame)
        # cv2.imshow("webcam_r", frame[:,:,0])
        # cv2.imshow("webcam_b", frame[:,:,2])
        # cv2.imshow("webcam_g", frame[:,:,1])

        mask = cv2.inRange(frame, (150,5,5), (255,100,100))

        cv2.imshow('mask',mask)
    except:
        print('an error occurred')

    key = cv2.waitKey(50)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
cv2.waitKey(50)