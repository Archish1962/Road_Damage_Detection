from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/runs/detect/rdd_train/weights/best.pt")

    metrics = model.val(
        data="data/rdd.yaml",
        imgsz=768,
        device=0
    )

    print("\n==== VALIDATION RESULTS ====")
    print(f"mAP50     : {metrics.box.map50:.4f}")
    print(f"mAP50-95  : {metrics.box.map:.4f}")
    print("Per-class mAP50:")
    for i, v in enumerate(metrics.box.maps):
        print(f"  Class {i}: {v:.4f}")

if __name__ == "__main__":
    main()
