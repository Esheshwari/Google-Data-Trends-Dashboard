import gspread
from google.oauth2.service_account import Credentials

# Define the scope for Sheets + Drive
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

# Load credentials.json
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

# Authorize client
client = gspread.authorize(creds)

# Your spreadsheet ID
SPREADSHEET_ID = "1qjDUWKspcFS8xcgj_QvTb9i2XK4GvC9zlpbEX4zc_bI"

# Open the sheet by ID
sheet = client.open_by_key(SPREADSHEET_ID)

# Select first worksheet
worksheet = sheet.sheet1

# ✅ Example 1: Read first row
row_data = worksheet.row_values(1)
print("First Row:", row_data)

# ✅ Example 2: Append new row
worksheet.append_row(["Hello", "from Python", "123"])

print("✅ Data added successfully!")
