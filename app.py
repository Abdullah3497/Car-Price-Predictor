import streamlit as st
import pandas as pd
import pickle

# ✅ Load trained model and column structure
with open("car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")
st.title("🚗 Car Price Predictor")
st.markdown("Enter the details below to predict the estimated car price.")

# 📥 User Inputs
category = st.selectbox("Category", ["3 Door", "4 Door", "5 Seater", "8 Seater"])
make = st.text_input("Car Make (Brand)", "Toyota")
model_name = st.text_input("Car Model", "Corolla")
city = st.selectbox("City", ["Lahore", "Islamabad", "Karachi", "Peshawar"])
year = st.number_input("Year", min_value=2000, max_value=2025, value=2021)
mileage = st.number_input("Mileage (in KM)", min_value=0, max_value=300000, value=35000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Hybrid", "Electric"])
engine = st.number_input("Engine Capacity (in CC)", min_value=600, max_value=8000, value=1800)
transmission = st.selectbox("Transmission", ["Automatic", "Manual"])

if st.button("🔍 Predict Price"):
    # 🔄 Prepare DataFrame
    input_dict = {
        'category': category,
        'make': make,
        'model': model_name,
        'city': city,
        'year': year,
        'mileage': mileage,
        'fuel': fuel,
        'engine': engine,
        'transmission': transmission
    }
    user_df = pd.DataFrame([input_dict])

    # 🧠 One-hot encode and align columns
    user_encoded = pd.get_dummies(user_df)
    user_encoded = user_encoded.reindex(columns=model_columns, fill_value=0)

    # 💰 Predict
    predicted_price = model.predict(user_encoded)[0]
    st.success(f"💰 Estimated Car Price: Rs. {predicted_price:,.0f}")
