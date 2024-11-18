import streamlit as st
import requests
import os

# Get API key from environment variable
api_key = os.getenv('EXCHANGE_API_KEY')

# Function to get real-time conversion rates using the API key
def get_conversion_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    
    response = requests.get(url)
    data = response.json()

    # Check if the response contains the rate
    if response.status_code == 200 and 'conversion_rates' in data:
        return data['conversion_rates'].get(to_currency)
    else:
        return None

# Streamlit UI
st.title("Currency Converter")

# Currency inputs
from_currency = st.selectbox("From Currency", ["USD", "EUR", "INR", "GBP", "AUD", "CAD", "JPY", "CNY"])
to_currency = st.selectbox("To Currency", ["USD", "EUR", "INR", "GBP", "AUD", "CAD", "JPY", "CNY"])
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

# Convert Button
if st.button("Convert"):
    if from_currency == to_currency:
        st.write("Please select different currencies for conversion.")
    else:
        rate = get_conversion_rate(from_currency, to_currency)
        if rate:
            converted_amount = amount * rate
            st.write(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.write("Conversion rate not available.")
