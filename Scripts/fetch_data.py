# fetch_trends.py
import os
import pandas as pd
from pytrends.request import TrendReq

# =============== CONFIG ===============
KEYWORDS = ["Google", "AI", "ChatGPT", "Python", "Microsoft"]
TIMEFRAME = "today 12-m"  # last 12 months
GEO = "IN"  # India (change to "US" for USA, etc.)
DATA_DIR = "data"
# ======================================

def fetch_trends():
    print("Connecting to Google Trends...")
    pytrends = TrendReq(hl="en-US", tz=330)

    # Build request
    pytrends.build_payload(KEYWORDS, cat=0, timeframe=TIMEFRAME, geo=GEO, gprop="")

    # Get interest over time
    df_trends = pytrends.interest_over_time()
    df_trends.reset_index(inplace=True)

    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Save file
    file_path = os.path.join(DATA_DIR, "trends_data.csv")
    df_trends.to_csv(file_path, index=False)

    print(f"✅ Data saved to {file_path}")

if __name__ == "__main__":
    fetch_trends()

