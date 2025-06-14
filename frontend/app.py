import streamlit as st

st.set_page_config(page_title="California House Price App", page_icon="🏠")

st.title("🏡 Welcome to California House Price Predictor")
st.markdown("""
This app predicts the **Median House Value** in California based on housing characteristics.

### 📌 Pages
- **Predict:** Enter input features and get price predictions.
- **About:** Learn more about the dataset and how the model works.
""")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Northern_California_landscape.jpg/1125px-Northern_California_landscape.jpg", use_container_width=True)

