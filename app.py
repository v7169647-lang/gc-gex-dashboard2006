import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="GC Gold GEX Dashboard",
    page_icon="🟡",
    layout="wide"
)

st.title("🟡 GC Gold GEX Dashboard")

try:
    headers = {
        "x-access-token": st.secrets["GOLD_API_KEY"]
    }

    response = requests.get(
        "https://www.goldapi.io/api/price/XAU/USD",
        headers=headers,
        timeout=10
    )

    data = response.json()

    st.metric(
        "Live Gold Price",
        f"{data['price']:.2f}"
    )

    st.json(data)
    
uploaded_file = st.file_uploader(
    "Upload VOI Excel",
    type=["xls", "xlsx"]
)

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("Excel Data")
    st.dataframe(df)

except Exception as e:
    st.error(f"Error: {e}")
