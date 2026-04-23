# import cv2
# import os
# import pandas as pd

# def load_yolo_label(label_path, img_w, img_h):
#     boxes = []
#     with open(label_path) as f:
#         for line in f:
#             cls, x, y, w, h = map(float, line.strip().split())
            
#             x1 = int((x - w/2) * img_w)
#             y1 = int((y - h/2) * img_h)
#             x2 = int((x + w/2) * img_w)
#             y2 = int((y + h/2) * img_h)

#             boxes.append((x1, y1, x2, y2))
#     return boxes

# def crop_dataset():
#     df = pd.read_csv("dataset/classifier/labels.csv")

#     for _, row in df.iterrows():
#         img_path = f"dataset/detection/images/train/{row['image']}"
#         label_path = f"dataset/detection/labels/train/{row['image'].rsplit('.', 1)[0] + '.txt'}"

#         img = cv2.imread(img_path)
#         h, w = img.shape[:2]

#         boxes = load_yolo_label(label_path, w, h)

#         for i, (x1, y1, x2, y2) in enumerate(boxes):
#             crop = img[y1:y2, x1:x2]

#             label = f"{row['country']}_{row['variant']}"
#             save_dir = f"dataset/classifier/crops/{label}"
#             os.makedirs(save_dir, exist_ok=True)

#             cv2.imwrite(f"{save_dir}/{row['image']}_{i}.jpg", crop)

# if __name__ == "__main__":
#     crop_dataset()





import cv2
import os
import pandas as pd

def load_yolo_label(label_path, img_w, img_h):
    boxes = []

    if not os.path.exists(label_path):
        print(f"Missing label: {label_path}")
        return boxes

    with open(label_path) as f:
        for line in f:
            cls, x, y, w, h = map(float, line.strip().split())

            x1 = int((x - w/2) * img_w)
            y1 = int((y - h/2) * img_h)
            x2 = int((x + w/2) * img_w)
            y2 = int((y + h/2) * img_h)

            # clamp
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(img_w, x2)
            y2 = min(img_h, y2)

            boxes.append((x1, y1, x2, y2))

    return boxes


def process_split(split):
    df = pd.read_csv("dataset/classifier/labels.csv")

    for _, row in df.iterrows():
        image_name = row["image"]

        img_path = f"dataset/detection/images/{split}/{image_name}"

        base = image_name.rsplit(".", 1)[0]
        label_path = f"dataset/detection/labels/{split}/{base}.txt"

        if not os.path.exists(img_path):
            continue

        img = cv2.imread(img_path)

        if img is None:
            print(f"Failed to load: {img_path}")
            continue

        h, w = img.shape[:2]

        boxes = load_yolo_label(label_path, w, h)

        for i, (x1, y1, x2, y2) in enumerate(boxes):
            crop = img[y1:y2, x1:x2]

            if crop.size == 0:
                print(f"Empty crop detected: {img_path}")
                continue

            label = f"{row['object']}_{row['country']}_{row['variant']}"
            save_dir = f"dataset/classifier/crops/{split}/{label}"
            os.makedirs(save_dir, exist_ok=True)

            save_path = f"{save_dir}/{base}_{i}.jpg"
            cv2.imwrite(save_path, crop)


def crop_dataset():
    for split in ["train", "val"]:
        print(f"Processing {split}...")
        process_split(split)

    print("Done.")


if __name__ == "__main__":
    crop_dataset()