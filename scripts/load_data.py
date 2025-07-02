import pandas as pd
import sqlite3
import os

def main():
    # file paths
    DATA_PATH = os.path.join("data", "customers.csv")
    DB_PATH = os.path.join("database", "customers.db")

    # read CSV
    df = pd.read_csv(DATA_PATH)

    # get rid off Index column if exists
    if 'Index' in df.columns:
        df = df.drop(columns=['Index'])

    # write to DB
    os.makedirs("../database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("customers", conn, if_exists="replace", index=False)

    print("Data is successfully uploaded to the table 'customers'.")
    print(f"Columns in the table: {len(df)}")

    conn.close()
