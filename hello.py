import streamlit as st
import pandas as pd
import os

# File path for local Excel storage
EXCEL_FILE = r"/Users/saiprasannavetapalem/Desktop/DataManager26_4_2025/python/data.xlsx"
SHEET_NAME = "Submissions"

# Page title
st.title("📋 Contact Form with Excel Storage")

# Input form
with st.form("contact_form", clear_on_submit=True):
    st.subheader("Enter your details")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Submit")

# On form submission
if submitted:
    # Prepare new row
    new_data = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])

    # If file exists, load it
    if os.path.exists(EXCEL_FILE):
        try:
            existing_data = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
            df = pd.concat([existing_data, new_data], ignore_index=True)
        except Exception as e:
            st.error(f"Error reading Excel: {e}")
            df = new_data
    else:
        df = new_data

    try:
        # Save updated data to Excel
        with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, sheet_name=SHEET_NAME, index=False)
        st.success("✅ Your response has been saved!")
    except Exception as e:
        st.error(f"Error writing to Excel: {e}")

# Display submitted data
if os.path.exists(EXCEL_FILE):
    st.subheader("📄 Submitted Data")
    try:
        submitted_df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
        st.dataframe(submitted_df)
    except Exception as e:
        st.error(f"Error reading Excel for display: {e}")
