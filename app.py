import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the sheet
sheet = client.open("streamlitapp").sheet1

# Streamlit app UI
st.title("📋 Streamlit + Google Sheets Form")

# Form fields
with st.form(key="form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit = st.form_submit_button("Submit")

    if submit:
        if name and email and message:
            # Append to Google Sheet
            sheet.append_row([name, email, message])
            st.success("✅ Submission successful!")
        else:
            st.error("❌ Please fill in all fields.")

# Display data table
st.subheader("📊 Current Submissions")
records = sheet.get_all_records()
if records:
    df = pd.DataFrame(records)
    st.dataframe(df)
else:
    st.info("No data yet.")
