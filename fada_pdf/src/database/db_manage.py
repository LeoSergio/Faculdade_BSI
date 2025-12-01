import sqlite3
import pandas as pd

DB_NAME = "database.sqlite"

def save_to_database(df: pd.DataFrame, table_name="historico"):
    print("💾 Salvando no banco SQLite...")

    conn = sqlite3.connect(DB_NAME)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    print(f"✔ Dados salvos na tabela '{table_name}'.")
