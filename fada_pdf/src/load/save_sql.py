#Salvar ou exportar dados(Salva no formato desejado que é o sql 1lite)
import pandas as pd
import sqlite3

def save_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str):
    """
    Salva o DataFrame no banco SQLite.
    """
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
