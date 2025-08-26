import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

# ------------------------
# 1. Google Sheets Setup
# ------------------------
SCOPE = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

CREDS = ServiceAccountCredentials.from_json_keyfile_name(
    r"C:\Users\HP\OneDrive\My Projects\Google Trends Insights Dashboard\Scripts\Credentials.json",
    SCOPE
)
CLIENT = gspread.authorize(CREDS)

# Open Google Sheet by ID (from URL)
SPREADSHEET_ID = "1JxnK-pgd3wE6m6zVlb9fBlzrvDPtoJl3fXImGcLNxoU"
SHEET = CLIENT.open_by_key(SPREADSHEET_ID).sheet1

# ------------------------
# 2. Function to fetch data
# ------------------------
def fetch_google_trends():
    """Dummy data for now."""
    data = {
        "Keyword": ["Python", "AI", "Data Science"],
        "Trend Score": [80, 95, 70],
        "Date": [datetime.now().strftime("%Y-%m-%d")] * 3
    }
    df = pd.DataFrame(data)
    return df

# ------------------------
# 3. Upload to Google Sheets
# ------------------------
def upload_to_sheets(df):
    rows = [df.columns.values.tolist()] + df.values.tolist()
    SHEET.clear()
    SHEET.update(rows)
    print("✅ Data uploaded successfully at", datetime.now())

# ------------------------
# 4. Main Execution
# ------------------------
if __name__ == "__main__":
    df = fetch_google_trends()
    upload_to_sheets(df)




