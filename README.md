# 🏡 California House Pricing Prediction – ML Pipeline with CI/CD and AWS Deployment

This project builds a production-ready machine learning pipeline to predict house prices using the **California Housing Dataset**. The pipeline is fully containerized with Docker, tracks experiments with MLflow, integrates CI/CD via GitHub Actions, and is deployed on an AWS EC2 Ubuntu instance.

---

## 🚀 Project Overview

### 📌 Phase 1: Model Training & Experiment Tracking

- **Dataset**: California Housing Dataset from Scikit-Learn
- **Goal**: Predict median house value based on various features like income, house age, population, etc.
- **Preprocessing**:
  - Handling missing values
  - Normalization & scaling
  - Feature engineering
- **Models Used**:
  - Linear Regression
  - Random Forest Regressor
- **Experiment Tracking**:
  - Logged metrics, parameters, and models with **MLflow**
- **Model Saving**:
  - Best model saved using `joblib`
- **Cloud Storage**:
  - Model optionally stored in **AWS S3** (if configured)

---

## 🧠 Phase 2: API, UI & Deployment

### 🛠 Backend (FastAPI)

- **Endpoints**:
  - `GET /health` → Health check
  - `POST /predict` → Returns price prediction
- **Loads**:
  - The trained `joblib` model from Phase 1

### 🎨 Frontend (Streamlit)

- Simple web interface for user input
- Connects to FastAPI backend for live predictions

---

## 🐳 Containerization (Docker)

- **Backend** and **Frontend** both containerized using Docker
- Docker Compose used to orchestrate both services

**docker-compose.yml**
```yaml
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
    depends_on:
      - backend
