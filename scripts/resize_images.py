import cv2
import os

def resize_images(input_dir, output_dir, size=(640, 640)):
    # Check input directory exists
    if not os.path.exists(input_dir):
        print(f"Input directory does not exist: {input_dir}")
        return

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"Reading from: {input_dir}")
    print(f"Saving to: {output_dir}")

    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)

        # Skip if it's not a file
        if not os.path.isfile(img_path):
            continue

        # Read image
        img = cv2.imread(img_path)

        # Skip if not a valid image
        if img is None:
            print(f"Skipping non-image file: {img_name}")
            continue

        # Resize image
        img_resized = cv2.resize(img, size)

        # Save resized image
        output_path = os.path.join(output_dir, img_name)
        cv2.imwrite(output_path, img_resized)

        print(f"Resized: {img_name}")
    print("Done resizing images!")


if __name__ == "__main__":
    # Get project root directory (one level up from /scripts)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_path = os.path.join(base_dir, "processing_data", "need to process still")
    output_path = os.path.join(base_dir, "processing_data", "good processed new batch")

    resize_images(input_path, output_path)