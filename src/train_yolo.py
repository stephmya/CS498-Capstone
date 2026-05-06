from ultralytics import YOLO
import torch

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu" #sanity
    print(f"Using device: {device}")

    model = YOLO("yolov8m.pt") #medium model, good balance of speed and accuracy
    # model = YOLO("yolov8n.pt") # small and fast but accuracy is meh
    # model = YOLO("yolov8s.pt") #^^


    model.train(
        data="dataset/data.yaml",
        epochs=10, # found 10 to be good balance
        imgsz=640,
        batch=16, # was good balance
        device=device,
        workers=4,
        name="object_detector",
    )

    print("YOLO training complete.")

if __name__ == "__main__":
    main()


# yolo is single stage end to end regression. single cnn, 1 pass, generally used for real time security/monitoring