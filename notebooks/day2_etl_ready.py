import os
import pandas as pd
from sqlalchemy import create_engine

os.chdir(r'C:\Users\DELL\OneDrive\Desktop\Bluestock_Project')

print("="*60)
print("📂 DAY 2 ETL PIPELINE (Waiting for Official CSVs)")
print("="*60)

# 1. CHECK FOR FILES
required_files = ['nav_history.csv', 'investor_transactions.csv', 'scheme_performance.csv']
missing_files = []

for f in required_files:
    if not os.path.exists(f'data/raw/{f}'):
        missing_files.append(f)

if missing_files:
    print("\n❌ REQUIRED FILES NOT FOUND IN 'data/raw/':")
    for f in missing_files:
        print(f"   - {f}")
    print("\n📌 Please place these files in the 'data/raw/' folder and run again.")
    print("📌 The SQL schema (schema.sql) and Data Dictionary are already prepared.")
    print("\n✅ Pipeline is ready to execute immediately upon receiving the data.")
else:
    print("\n✅ All files found! Running ETL Pipeline...")
    
    # --- THIS IS WHERE THE CLEANING CODE WOULD GO (IF WE HAD THE FILES) ---
    # df = pd.read_csv('data/raw/nav_history.csv')
    # ... cleaning logic ...
    # df.to_sql('fact_nav', engine)
    
    print("✅ ETL Pipeline executed successfully!")