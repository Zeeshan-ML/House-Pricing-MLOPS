import streamlit as st
import requests

st.title("📊 Predict California House Price")

st.markdown("### 🔢 Enter House Features")

with st.form("prediction_form"):
    MedInc = st.number_input("Median Income", min_value=0.0, value=8.3252)
    HouseAge = st.number_input("House Age", min_value=0.0, value=41.0, format="%.0f")
    AveRooms = st.number_input("Average Rooms", min_value=0.0, value=6.984127)
    AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.023810)
    Population = st.number_input("Population", min_value=0.0, value=322.0)
    AveOccup = st.number_input("Average Occupants", min_value=0.0, value=2.555556)
    Latitude = st.number_input("Latitude", min_value=0.0, value=37.88)
    Longitude = st.number_input("Longitude", min_value=-180.0, value=-122.23)
    
    submit = st.form_submit_button("Predict")

if submit:
    features = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude,
    }

    with st.spinner("Predicting..."):
        try:
            response = requests.post("http://backend:8000/predict", json=features)
            if response.status_code == 200:
                price = response.json()['predicted_price']
                st.success(f"🏠 Predicted Median House Price: ${price * 100000:.2f}")
            else:
                st.error("❌ Prediction failed. Is the FastAPI server running?")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
