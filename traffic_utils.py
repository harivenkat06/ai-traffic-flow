from ultralytics import YOLO
import cv2
import pandas as pd
import os

model = YOLO("yolov8n.pt")  # You can replace with yolov8s.pt for better accuracy
VEHICLE_CLASSES = ['car', 'bus', 'truck', 'motorbike', 'bicycle']

def detect_vehicles(image_path):
    """Detect vehicles and return annotated image + count."""
    image = cv2.imread(image_path)
    results = model(image)
    detections = results[0].boxes.data

    vehicle_count = 0
    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        label = model.names[int(cls)]
        if label in VEHICLE_CLASSES:
            vehicle_count += 1
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
            cv2.putText(image, f"{label}", (int(x1), int(y1)-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    return image, vehicle_count


def get_density_level(vehicle_count):
    if vehicle_count <= 5:
        return "Low Traffic"
    elif 6 <= vehicle_count <= 15:
        return "Moderate Traffic"
    else:
        return "High Traffic"


def suggest_signal(density_level):
    if density_level == "Low Traffic":
        return "Green light for 20 seconds"
    elif density_level == "Moderate Traffic":
        return "Green light for 40 seconds"
    else:
        return "Green light for 60 seconds"


def log_result(vehicle_count, density):
    """Save result to CSV for trend analysis."""
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame([{
        "vehicle_count": vehicle_count,
        "density_level": density,
        "timestamp": pd.Timestamp.now()
    }])
    csv_path = "data/traffic_log.csv"
    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_path, index=False)
