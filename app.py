import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SIP Calculator", layout="centered")

st.title("📈 SIP Calculator Dashboard")

monthly_sip = st.number_input("Monthly SIP Amount (₹)", min_value=500, step=500, value=5000)
annual_return = st.slider("Expected Annual Return (%)", 1, 30, 12)
years = st.slider("Investment Period (Years)", 1, 40, 10)

months = years * 12
monthly_rate = annual_return / 100 / 12

future_value = monthly_sip * ((1 + monthly_rate) ** months - 1) / monthly_rate * (1 + monthly_rate)
total_invested = monthly_sip * months
gain = future_value - total_invested

st.subheader("📊 Investment Summary")
st.write(f"**Total Invested:** ₹{total_invested:,.0f}")
st.write(f"**Estimated Value:** ₹{future_value:,.0f}")
st.write(f"**Total Gain:** ₹{gain:,.0f}")

data = {
    "Type": ["Invested", "Gain"],
    "Amount": [total_invested, gain]
}

df = pd.DataFrame(data)

st.subheader("📉 Investment Breakdown")
st.bar_chart(df.set_index("Type"))
