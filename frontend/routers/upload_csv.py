import streamlit as st
import pandas as pd

def render():
    st.title("📤 Upload CSV File")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")
            st.dataframe(df)

            # Optionally: Save to disk
            # with open("uploaded_file.csv", "wb") as f:
            #     f.write(uploaded_file.getbuffer())

        except Exception as e:
            st.error(f"❌ Error reading CSV: {e}")
    else:
        st.info("📎 Please upload a CSV file.")
