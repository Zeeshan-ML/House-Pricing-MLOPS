import gdown
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Google Drive file ID and local model filename
FILE_ID = "11OWNGXfQL4HMUiRKOMy6c0-UifTZr1j-"  # replace with your actual file ID
MODEL_PATH = "model.pkl"

# Load the model on startup
@app.on_event("startup")
def load_model():
    # Download the model file from Google Drive if not already present
    import os
    if not os.path.exists(MODEL_PATH):
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

    global model
    model = joblib.load(MODEL_PATH)

# Input schema for prediction
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Prediction endpoint
@app.post("/predict")
def predict(features: HouseFeatures):
    df = pd.DataFrame([features.dict()])
    prediction = model.predict(df)[0]
    return {"predicted_price": prediction}
