# Road Damage Detection using YOLOv8 (RDD2022)

This repository contains the complete **source code** for an object detection system built using **YOLOv8** to detect and classify road damage from images.

The model detects **five classes of road damage**:
- Longitudinal Crack
- Transverse Crack
- Alligator Crack
- Other Corruption
- Pothole

---

## Repository Contents
```
.
├── scripts/
│ ├── check_dataset.py
│ ├── train.py
│ ├── validate.py
│ ├── predict_test.py
│ └── fill_missing_predictions.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Environment Setup

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## GPU Support (Optional)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Model Training
```bash
python scripts/train.py
```

## Validation
```bash
python scripts/validate.py
```

## Test Inference
```bash
python scripts/predict_test.py
```

### Predictions are saved in YOLO format:

```
<class_id> <x_center> <y_center> <width> <height> <confidence>
```


