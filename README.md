# SciFarm
# 🌱 Crop Recommendation Web App

This is a Flask-based web application that predicts the most suitable crop to cultivate based on environmental factors like soil nutrients, temperature, humidity, pH, and rainfall. The model uses machine learning for accurate predictions.

---

## 🚀 Features

- Predicts the best crop to grow based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - Soil pH
  - Rainfall (mm)
- Clean and responsive UI with HTML & CSS
- Trained ML model using `scikit-learn`
- Deployed using [Render](https://render.com)

---

## 🧠 Tech Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python, Flask
- **ML Libraries**: `scikit-learn`, `numpy`, `pandas`
- **Deployment**: Render
- **Model Files**:
  - `model.pkl` (Decision Tree Classifier)
  - `standscaler.pkl` (Standard Scaler)
  - `minmaxscaler.pkl` (MinMax Scaler)

---
