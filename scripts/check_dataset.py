import os

def check_split(split):
    img_dir = f"data/{split}/images"
    lbl_dir = f"data/{split}/labels"

    if split != "test" and not os.path.exists(lbl_dir):
        raise FileNotFoundError(f"Missing labels directory for {split}")

    images = set(os.listdir(img_dir))
    labels = set(os.listdir(lbl_dir)) if split != "test" else set()

    if split != "test":
        missing = [img for img in images if img.replace(".jpg", ".txt") not in labels]
        if missing:
            raise ValueError(f"{split}: Missing labels for {len(missing)} images")

    print(f"{split} split OK")

if __name__ == "__main__":
    for s in ["train", "val", "test"]:
        check_split(s)
