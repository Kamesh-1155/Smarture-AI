import streamlit as st
import pickle
import os
import matplotlib.pyplot as plt

from utils.predictor import predict_top_crops
from utils.recommender import recommend_best_crop, crop_price
from utils.explanation import generate_explanation

# ------------------ Load Model ------------------
if not os.path.exists("model.pkl"):
    st.error("❌ model.pkl not found! Please run model.py first.")
    st.stop()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ------------------ Banner ------------------
logo_path = os.path.join("assets", "logo.png")
st.image(logo_path, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### 🌱 AI Crop Recommendation System")
st.caption("Predict the best🔥 and most profitable💎 crop using AI")

# ------------------ Inputs ------------------
st.subheader("📥 Enter Soil & Weather Details👇🏼")

N = st.number_input("Nitrogen (N)", 0, 140)
P = st.number_input("Phosphorus (P)", 0, 140)
K = st.number_input("Potassium (K)", 0, 200)
temp = st.number_input("Temperature (°C)", 0.0, 50.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0)
ph = st.number_input("pH Value", 0.0, 14.0)
rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0)

# ------------------ Prediction ------------------
if st.button("🚀 Run AI Recommendation"):

    top_crops = predict_top_crops(model, N, P, K, temp, humidity, ph, rainfall)
    best_crop = recommend_best_crop(top_crops)

    # ------------------ Results ------------------
    st.success(f"🌾 Best Crop (AI Recommended): **{best_crop.upper()}**")

    st.subheader("📊 Top 3 Suitable Crops")
    for crop, prob in top_crops:
        st.write(f"• {crop} → {round(prob * 100, 2)}% confidence")

    # ------------------ Explanation ------------------
    st.subheader("🧠 AI Explanation")
    explanation = generate_explanation(best_crop, temp, rainfall, ph)
    st.info(explanation)

    # ------------------ Graphs ------------------

    crops = [crop for crop, prob in top_crops]
    probs = [prob * 100 for crop, prob in top_crops]
    profits = [crop_price.get(crop, 10) for crop in crops]

    col1, col2 = st.columns(2)

    # 📊 Confidence Graph
    with col1:
        st.subheader("📊 Prediction Confidence")
        fig1, ax1 = plt.subplots()
        ax1.bar(crops, probs)
        ax1.set_xlabel("Crops")
        ax1.set_ylabel("Confidence (%)")
        ax1.set_title("Top Crop Predictions")
        st.pyplot(fig1)

    # 💰 Profit Graph
    with col2:
        st.subheader("💰 Profit Comparison")
        fig2, ax2 = plt.subplots()
        ax2.bar(crops, profits)
        ax2.set_xlabel("Crops")
        ax2.set_ylabel("Price (₹/kg)")
        ax2.set_title("Estimated Market Value")
        st.pyplot(fig2)

# ------------------ Footer ------------------
st.markdown("---")
st.caption("🌾 Smarture | AI + Machine Learning for Smart Farming")