import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Step 1: Define the scopes for Google Sheets and Drive API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Step 2: Load credentials from the JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

# Step 3: Authorize gspread with the credentials
client = gspread.authorize(creds)

# Step 4: Open your Google Sheet by name
sheet = client.open("streamlitapp").sheet1

# Step 5: Fetch all records as a list of dictionaries
data = sheet.get_all_records()

# Step 6: Print the data
print(data)
