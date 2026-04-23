import os


def title_images(input_dir, prefix, digits=2, extension=None):
    print(f"Renaming files in: {input_dir}")

    normalized_extension = f".{extension.lower()}" if extension else None

    for index, name in enumerate(sorted(os.listdir(input_dir), key=str.lower), start=1):
        old_path = os.path.join(input_dir, name)

        if not os.path.isfile(old_path):
            continue

        if normalized_extension and os.path.splitext(name)[1].lower() != normalized_extension:
            continue

        new_name = f"{prefix}-{index:0{digits}d}{os.path.splitext(name)[1]}"
        new_path = os.path.join(input_dir, new_name)

        os.rename(old_path, new_path)

        print(f"renamed: {name}")

    print("done")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_path = os.path.join(base_dir, "processing_data", "raw_images", "india_1_sidewalks_raw")

    title_images(input_path, "sidewalks_1_india", 2, None)