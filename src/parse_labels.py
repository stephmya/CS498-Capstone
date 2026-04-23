import os
import pandas as pd

#gets rid of the file # suffix so its grouped by variants and not file #
def clean_variant(v):
    return v.split("-")[0] if v else None

## structuring of the csv
def parse_filename(filename, split):
    base = filename.rsplit(".", 1)[0]
    parts = base.split("_")

    return {
        "image": filename,
        "split": split,   
        "object": parts[0],
        "country": parts[1],
        "variant": clean_variant(parts[2])    }

#csvbuilder func, reads image folders and labels
def build_csv(base_dir, output_csv):
    rows = []

    for split in ["train", "val"]:
        image_dir = os.path.join(base_dir, split)

        if not os.path.exists(image_dir): #make sure its real
            print(f"Missing folder: {image_dir}")
            continue

        files = os.listdir(image_dir) #list of files in the folder
        print(f" {split}: {len(files)} files") #number of files in folder

        for f in files: #thru all
            if f.lower().endswith(".png"):
                parsed = parse_filename(f, split)
                if parsed is not None:
                    rows.append(parsed)

    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)

    print(df["split"].value_counts())


if __name__ == "__main__":
    build_csv(
        "dataset/detection/images/",
        "dataset/classifier/labels.csv"
    )