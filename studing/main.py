import cv2
import numpy as np


def create_taskbar():
    cv2.namedWindow('Trackbars')
    cv2.createTrackbar("L - hue", "Trackbars", 1,179, lambda  x:None)
    cv2.createTrackbar("L - saturation", "Trackbars", 52, 255, lambda x: None)
    cv2.createTrackbar("L - value", "Trackbars", 64, 255, lambda x: None)
    cv2.createTrackbar("H - hue", "Trackbars", 24,255, lambda  x:None)
    cv2.createTrackbar("H - saturation", "Trackbars", 161, 255, lambda x: None)
    cv2.createTrackbar("H - value", "Trackbars", 242, 255, lambda x: None)

def apply_hsv_filter():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    create_taskbar()

    while True:
        ret , frame = cap.read()
        if not ret:
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('hsv', hsv_frame)
        cv2.waitKey(1)

        lh = cv2.getTrackbarPos("L - hue", "Trackbars")
        ls = cv2.getTrackbarPos("L - saturation", "Trackbars")
        lv = cv2.getTrackbarPos("L - value", "Trackbars")
        hh = cv2.getTrackbarPos("H - hue", "Trackbars")
        hs = cv2.getTrackbarPos("H - saturation", "Trackbars")
        hv = cv2.getTrackbarPos("H - value","Trackbars")

        lower_bound = np.array([lh, ls, lv])
        upper_bound = np.array([hh, hs, hv])

        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)


        kernel = np.ones((5, 5), np.uint8)

        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        cv2.imshow("mask HSV", mask)







        kernel = np.ones((41,41 ), np.uint8)
        mask_hand = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        kernel = np.ones((7  ,7), np.uint8)
        # mask_hand = cv2.morphologyEx(mask_hand, cv2.MORPH_CLOSE, kernel)

        mask_fingers = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask_fingers = cv2.morphologyEx(mask_fingers, cv2.MORPH_OPEN, kernel)


        mask_finnish = cv2.absdiff(mask_fingers, mask_hand)

        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask_finnish, connectivity=8)+++

        print(num_labels)

        output = frame.copy()
        for i in range(1, num_labels):
            x,y,w,h, area = stats[i]
            if area > 400:
                cv2.rectangle(output, (x,y), (x + w, y+h), (0,255,0), 2)
                cv2.putText(output, f"ID :[i]", (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        cv2.imshow("mask_hand", mask_finnish)
        cv2.imshow("mask_output", output)

if __name__ == "__main__":
    apply_hsv_filter()

