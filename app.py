import streamlit as st
import cv2
import tempfile
import pandas as pd
from traffic_utils import detect_vehicles, get_density_level, suggest_signal, log_result

st.set_page_config(page_title="AI Traffic Monitoring", layout="wide")

st.title("🚦 AI-Based Traffic Congestion Monitoring System")

uploaded_file = st.file_uploader("Upload a traffic image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())

    st.write("Analyzing image...")
    processed_image, vehicle_count = detect_vehicles(temp_file.name)
    density = get_density_level(vehicle_count)
    signal = suggest_signal(density)

    # Convert OpenCV image (BGR → RGB)
    processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)

    # Display results side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(processed_image, caption="Processed Image", use_container_width=True)
    with col2:
        st.metric("Vehicles Detected", vehicle_count)
        st.metric("Traffic Density", density)
        st.metric("Signal Suggestion", signal)

    # Log result
    log_result(vehicle_count, density)
    st.success("✅ Result logged successfully!")

# --- Traffic Trend Analysis Section ---
st.subheader("📈 Traffic Trend Analysis")

try:
    df = pd.read_csv("data/traffic_log.csv")
    st.line_chart(df, x="timestamp", y="vehicle_count", use_container_width=True)
except FileNotFoundError:
    st.info("No traffic history yet. Upload an image to start logging data.")
