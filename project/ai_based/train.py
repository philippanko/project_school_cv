from ultralytics import YOLO
import torch


def main():
    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

    # Load a model
    model = YOLO("yolo11n-cls.yaml")  # build a new model from YAML
    model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolo11-cls.yaml").load("yolo11n-cls.pt")  # build from YAML and transfer weights
    model.train(
        data="dataset",
        epochs=100,
        imgsz=640,
        batch=16,
        lr0=0.01,
        patience=5,
        project="runs",
        name="hazard_cls",
        pretrained=True,
        workers=8,
        verbose = False,
        augment=True
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # Optional on Windows
    main()
