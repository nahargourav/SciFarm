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

## 📁 Project Structure

```
├── app.py                  # Main Flask app
├── model.pkl               # Trained ML model
├── standscaler.pkl         # StandardScaler object
├── minmaxscaler.pkl        # MinMaxScaler object
├── templates/
│   └── web.html            # Frontend HTML page
├── static/                 # Optional: for CSS or JS
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/crop-recommendation-app.git
   cd crop-recommendation-app
   ```

2. **Create virtual environment & install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   https://scifarm.onrender.com/
   ```

---

## 🌐 Deploy on Render

1. Create a new Web Service on [Render](https://render.com).
2. Connect your GitHub repo.
3. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
4. Add Python version and dependencies in `requirements.txt`.

---

## 📦 requirements.txt (sample)

```txt
Flask==2.2.5
numpy
pandas
scikit-learn==1.2.2
gunicorn
```

---

## 🙏 Acknowledgments

- Inspired by real-world agriculture challenges
- ML Dataset from Kaggle 

---

## 📸 Preview

![App Screenshot](![image](https://github.com/user-attachments/assets/c73d8e78-0393-4ad9-bc86-273bf27b1e45)
) <!-- Add your screenshot image -->

---

## 📬 Contact

Created with 💚 by Gourav Nahar  
📧 gouravnahar3008@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/nahargourav)

```
