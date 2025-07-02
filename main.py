# This file runs load_data.py then runs app.py

import subprocess
import os
from scripts import load_data

def run_etl():
    print("Running ETL: loading data into SQLite...")
    load_data.main()
    print("ETL completed!")

def run_dashboard():
    print("Launching streamlit dashboard...")
    app_path = os.path.join("dashboard", "app.py")
    subprocess.run(["streamlit", "run", app_path])

if __name__ == "__main__":
    run_etl()
    run_dashboard()