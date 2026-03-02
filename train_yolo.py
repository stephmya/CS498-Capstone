from ultralytics import YOLO
import torch
import os

def main():
    device = 0 if torch.cuda.is_available() else "cpu"
    print("Using device:", device)

    model = YOLO("yolov8m.pt")
    # model = YOLO("yolov8n.pt")
    # model = YOLO("yolov8s.pt")

    # Train
    model.train(
        data="data.yaml",
        epochs=20,
        imgsz=640,
        batch=16,
        device=device,
        workers=4,
        name="bollard_detect",
        project="runs/detect"
    )

    print("Training complete.")

if __name__ == "__main__":
    main()