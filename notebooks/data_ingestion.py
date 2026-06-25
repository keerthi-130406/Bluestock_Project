import pandas as pd
import json
import os

os.chdir(r'C:\Users\DELL\OneDrive\Desktop\Bluestock_Project')

# --- Load the Master JSON you saved ---
with open('data/raw/master.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# --- Task 5: Profiling ---
print("="*50)
print("TASK 5: Data Profiling")
print("="*50)
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Columns: {df.columns.tolist()}")
print("\nFirst 5 rows:")
print(df.head())

# --- Task 8 & 9: Explore & Validate ---
print("\n" + "="*50)
print("TASK 8 & 9: Exploration & Validation")
print("="*50)
print(f"Unique Schemes in Master: {df['schemeCode'].nunique()}")

# Check your 5 codes
my_codes = ['119551', '120503', '118632', '119092', '120841']
master_codes = set(df['schemeCode'].astype(str))
matched = master_codes.intersection(set(my_codes))

print(f"Your 5 schemes matched in Master: {len(matched)} out of 5")
print("\nDATA QUALITY SUMMARY:")
print(f"- Total records: {df.shape[0]}")
print(f"- Missing values: {df.isnull().sum().sum()}")
print(f"- Duplicates: {df.duplicated().sum()}")
print("✅ Data ingestion and validation complete.")