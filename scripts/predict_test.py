from ultralytics import YOLO
import os
from pathlib import Path

def main():
    model = YOLO("runs/detect/runs/detect/rdd_train/weights/best.pt")

    test_images = "data/test/images"
    output_dir = "submission/predictions"

    os.makedirs(output_dir, exist_ok=True)

    model.predict(
        source=test_images,
        imgsz=768,
        conf=0.25,          # Confidence threshold
        iou=0.7,
        save=False,
        save_txt=True,
        save_conf=True,
        project="submission",
        name="predictions",
        exist_ok=True
    )

    print("Test inference complete.")
    print(f"Prediction files saved to: {output_dir}")

if __name__ == "__main__":
    main()
