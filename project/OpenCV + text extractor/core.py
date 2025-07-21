import cv2

def detect_squares():
    cam = cv2.VideoCapture(0)

    while True:
        # success, frame = cam.read()
        frame = cv2.imread("Screenshot 2025-07-06 141758.png")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        alpha = 1.5  # >1 — усилить контраст; <1 — уменьшить
        beta = 0  # 0 — не менять яркость
        gray = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
        edges = cv2.Canny(gray, 85, 95)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        min_size = 70  # пикселей, можно увеличить



        for contour in contours:
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                if w > min_size or h > min_size and w*h == min_size*min_size*1.2:
                    aspect_ratio = float(w) / h

                    if 1.3 > aspect_ratio > 0.7:
                        cv2.drawContours(frame, [approx], 0, (0, 255, 0), 5)
                        cv2.putText(frame, str(aspect_ratio), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                        print(approx)

        cv2.imshow("Shapes", frame)

        cv2.waitKey(50000)

    # Draw the contour and label the shape

# # Display the output
# cv2.waitKey(0)
# cv2.destroyAllWindows()

