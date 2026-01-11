from ultralytics import YOLO
import torch

def main():
    # Safety check: CUDA availability
    assert torch.cuda.is_available(), "CUDA not available — GPU not detected"
    device = 0
    print(f"Using device: {device}")

    model = YOLO("runs/detect/runs/detect/rdd_train/weights/last.pt")

    model.train(
        data="data/rdd.yaml",
        epochs=30,
        imgsz=768,
        batch=16,
        device=0,
        workers=6,
        amp=True,
        cache=False,
        resume=True,              # Resume training from last.pt
        project="runs/detect",
        name="rdd_train",
        exist_ok=True
    )


if __name__ == "__main__":
    main()
