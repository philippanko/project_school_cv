import cv2
from ultralytics import YOLO
import numpy as np
import mss

def detect_squares():
    model = YOLO("runs/hazard_cls2/weights/best.pt")
    print(model.names)
    cv2.namedWindow("detected")
    position = (10, 100)  # x, y
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 4
    color = (255, 255, 255)  # White
    thickness = 10
    width, height = (1920,150)

    # Put the text on the image

    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Основной монитор
        while True:
            image = np.zeros((height, width, 3), dtype=np.uint8)
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            results = model.predict(source=frame, imgsz=640, verbose=False)

            # 3. Extract prediction result
            probs = results[0].probs  # this holds class probabilities

            # 4. Print result
            class_id = probs.top1  # integer class ID
            confidence = probs.top1conf  # float confidence


            if confidence > 0.9 and class_id !=1:
                class_name = results[0].names[class_id]  # class label from model
                print(f"Detected {class_name} with confidence {confidence:.2f}")
                text = f'Detected: {class_name}'
                cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
            else:
                text = 'no sign detected'
                cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

            cv2.imshow("detected", image)

            cv2.waitKey(1)




        # 2. Run prediction on a single image


if __name__ == "__main__":
    detect_squares()
