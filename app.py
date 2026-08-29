import streamlit as st
import requests

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

except Exception as e:
    st.error(f"Error: {e}")
