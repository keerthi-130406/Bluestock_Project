import requests
import pandas as pd
from datetime import datetime
import os
import time

# Set working directory
os.chdir(r'C:\Users\DELL\OneDrive\Desktop\Bluestock_Project')

# --- Task 6 & 7: Fetch NAV for 5 schemes ---
scheme_codes = [119551, 120503, 118632, 119092, 120841]  # Your 5 codes
all_data = []

print("Fetching NAV for 5 schemes...")
for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            df = pd.DataFrame(data['data'])
            df['scheme_code'] = code
            df['scheme_name'] = data['meta'].get('scheme_name', 'Unknown')
            all_data.append(df)
            print(f"✅ Fetched {len(df)} rows for {code}")
    time.sleep(0.5)

if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    file_name = f"nav_5_schemes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    final_df.to_csv(f"data/raw/{file_name}", index=False)
    print(f"✅ Saved: {file_name}")