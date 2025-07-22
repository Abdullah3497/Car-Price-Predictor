# 🚗 Car Price Prediction using XGBoost

This project uses machine learning (XGBoost Regressor) to predict used car prices based on specifications such as make, model, engine capacity, mileage, transmission type, fuel type, and more.
A Streamlit web app is also included for interactive price prediction.

---

## 📂 Project Structure
car-price-predictor/
├── app.py # Streamlit app for live prediction
├── train_model.py # Data cleaning, training, visualization
├── car_listings.csv # Dataset (from local or scraped source)
├── car_price_model.pkl # Trained XGBoost model (binary format)
├── model_columns.pkl # Saved feature column names
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 📊 Dataset

The dataset `car_listings.csv` includes the following features:

- `category` – e.g., "5 Seater", "3 Door"
- `title` – raw name (from which brand/model is extracted)
- `city` – location of the car
- `year` – model year
- `mileage` – in KM (cleaned from text)
- `fuel` – Petrol, Diesel, Hybrid, etc.
- `engine` – CC (cleaned from text)
- `transmission` – Automatic or Manual
- `price` – Target column (to predict)

---

## 🔍 Features Used for Training

After cleaning and processing, the model uses:

- `category`
- `make` (from `title`)
- `model` (from `title`)
- `city`
- `year`
- `mileage`
- `fuel`
- `engine`
- `transmission`

---

## 🧠 Model

- **Algorithm**: XGBoost Regressor
- **Encoding**: One-hot encoding for categorical variables
- **Missing Handling**: Mean imputation
- **Evaluation**:
  - **RMSE**
  - **R² Score**
  - Actual vs. Predicted Price plot
  - Feature Importance Bar Chart

---

## 📈 Visualizations

Included in `train_model.py`:
- 📉 Actual vs Predicted Scatter Plot
- 📊 Feature Importance Bar Chart

---

## 🚀 Streamlit App

Run the web app with:
```bash
streamlit run app.py
The app allows users to input:

Category

Make and Model

City

Year

Mileage

Fuel Type

Engine Capacity

Transmission

It then predicts the estimated car price using the trained model.
