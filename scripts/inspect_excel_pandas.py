import pandas as pd
import os
import sys
import datetime

def inspect_excel_robust(path):
    print(f"--- Inspecting: {path} ---")
    if not os.path.exists(path):
        print("File does NOT exist.")
        return

    stats = os.stat(path)
    # File size
    print(f"File Size: {stats.st_size} bytes")
    # Mod time
    mod_time = datetime.datetime.fromtimestamp(stats.st_mtime)
    print(f"Last Modified: {mod_time}")

    print("\n--- Pandas Inspection ---")
    try:
        xl = pd.ExcelFile(path)
        print(f"Sheet Names: {xl.sheet_names}")
        
        for sheet in xl.sheet_names:
            df = xl.parse(sheet)
            print(f"\nSheet: '{sheet}'")
            print(f"  Shape: {df.shape}")
            print(f"  Columns: {df.columns.tolist()}")
            if not df.empty:
                print(f"  First Row Data: {df.iloc[0].tolist()}")
    except Exception as e:
        print(f"Pandas Error: {e}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "reports/raw.xlsx"
    inspect_excel_robust(path)
