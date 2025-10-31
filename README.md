# 🚦 AI-Based Traffic Signal Duration Control

An intelligent traffic management system that uses computer vision to analyze vehicle density in real-time and automatically adjust traffic signal durations.  
The project detects and counts vehicles in each lane from live camera feeds or video footage, optimizing green light timing based on current traffic conditions.

---

## 📋 Features

- 🧠 **Vehicle Detection:** Detects cars, buses, bikes, and trucks using deep learning (e.g., YOLO / MobileNet).
- 🚗 **Vehicle Counting:** Counts the number of vehicles in each frame or lane.
- ⏱️ **Dynamic Signal Timing:** Calculates optimal green signal duration based on traffic density.
- 🕒 **Real-Time Processing:** Works on live video or pre-recorded traffic footage.
- 📊 **Traffic Analysis Dashboard (optional):** Displays detected vehicles and computed signal durations.

---

## 🧰 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Programming Language** | Python |
| **Computer Vision** | OpenCV |
| **Machine Learning Model** | YOLO / TensorFlow / Haar Cascade |
| **Data Processing** | NumPy, Pandas |
| **Visualization (optional)** | Streamlit / Matplotlib |
| **Web Dashboard (optional)** | Flask or Streamlit |

---

## 🧪 How It Works

1. **Capture Frame:** Read a video frame from a traffic camera.
2. **Detect Vehicles:** Use a trained object detection model to identify and count vehicles.
3. **Calculate Traffic Density:** Determine how crowded each lane is.
4. **Decide Signal Duration:** Compute an optimal green light duration using a custom formula (e.g., proportional to vehicle count).
5. **Display Output:** Show vehicle counts, lane density, and recommended signal timings.

---

## ⚙️ Example Formula

```python
# Example duration logic
base_time = 15  # base green signal time in seconds
extra_time_per_vehicle = 2
green_time = base_time + (vehicle_count * extra_time_per_vehicle)
