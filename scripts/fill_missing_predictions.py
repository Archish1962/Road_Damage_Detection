import os
from pathlib import Path

# Paths
test_images_dir = Path("data/test/images")
pred_dir = Path("submission/predictions")

pred_dir.mkdir(parents=True, exist_ok=True)

# Get image base names (without extension)
image_names = {img.stem for img in test_images_dir.iterdir() if img.suffix.lower() in [".jpg", ".png", ".jpeg"]}

# Get prediction base names
pred_names = {pred.stem for pred in pred_dir.iterdir() if pred.suffix == ".txt"}

# Find missing prediction files
missing = image_names - pred_names

print(f"Total test images       : {len(image_names)}")
print(f"Prediction files exist  : {len(pred_names)}")
print(f"Missing prediction files: {len(missing)}")

# Create empty txt files for missing predictions
for name in missing:
    (pred_dir / f"{name}.txt").touch()

print("Empty prediction files created for missing images.")
