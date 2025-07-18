import cv2
from mss import mss


cam = cv2.VideoCapture(0)

while True:


    success, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 100)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    min_size = 50  # пикселей, можно увеличить
    min_square = 50



    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            if w > min_size or h > min_size and w*h > min_square:
                aspect_ratio = float(w) / h
                shape_name = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"


                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 5)
                cv2.putText(frame, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("Shapes", frame)

    cv2.waitKey(50)

    # Draw the contour and label the shape

# Display the output
cv2.waitKey(0)
cv2.destroyAllWindows()