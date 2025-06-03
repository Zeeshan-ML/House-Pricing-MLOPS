import streamlit as st #ignore
import requests

st.title("🏠 California House Price Predictor")

st.write("Enter the following features to predict the house price:")

features = {
    "MedInc": st.number_input("Median Income", min_value=0.0),
    "HouseAge": st.number_input("House Age", min_value=0.0),
    "AveRooms": st.number_input("Average Rooms", min_value=0.0),
    "AveBedrms": st.number_input("Average Bedrooms", min_value=0.0),
    "Population": st.number_input("Population", min_value=0.0),
    "AveOccup": st.number_input("Average Occupants", min_value=0.0),
    "Latitude": st.number_input("Latitude", min_value=0.0),
    "Longitude": st.number_input("Longitude", min_value=-180.0),
}

if st.button("Predict"):
    with st.spinner("Predicting..."):
        response = requests.post("http://127.0.0.1:8000/predict", json=features)
        if response.status_code == 200:
            price = response.json()['predicted_price']
            st.success(f"🏡 Predicted Median House Price: ${price * 100000:.2f}")
        else:
            st.error("Prediction failed. Check if the FastAPI server is running.")
