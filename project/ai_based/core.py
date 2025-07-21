from ultralytics import YOLO
import cv2



def detect_squares():
    cam = cv2.VideoCapture(0)
    model = YOLO("runs/hazard_cls2/weights/best.pt")  # adjust path if needed

    while True:
        success, frame = cam.read()
        results = model.predict(source=frame, imgsz=224)

        # 3. Extract prediction result
        probs = results[0].probs  # this holds class probabilities

        # 4. Print result
        class_id = probs.top1  # integer class ID
        confidence = probs.top1conf  # float confidence

        if confidence > 0.85:
            class_name = results[0].names[class_id]  # class label from model
            print(f"Detected {class_name} with confidence {confidence:.2f}")



        # 2. Run prediction on a single image


if __name__ == "__main__":
    detect_squares()
