import cv2
import os

def resize_images(input_dir, output_dir, size=(640, 640)):
    os.makedirs(output_dir, exist_ok=True)

    print(f"Reading from: {input_dir}")
    print(f"Saving to: {output_dir}")

    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)

        if not os.path.isfile(img_path):
            continue

        img = cv2.imread(img_path)

        if img is None:

            continue

        img_resized = cv2.resize(img, size)

        output_path = os.path.join(output_dir, img_name)
        cv2.imwrite(output_path, img_resized)

        print(f"Resized: {img_name}")
    print("Done resizing images!")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_path = os.path.join(base_dir, "processing_data", 'raw_images', "india_1_sidewalks_raw")
    output_path = os.path.join(base_dir, "processing_data", "india_1_sidewalks_resized")

    resize_images(input_path, output_path)