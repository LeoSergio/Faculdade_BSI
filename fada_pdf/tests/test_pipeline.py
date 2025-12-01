import sqlite3
import pandas as pd
from src.main import run_pipeline

def test_pipeline():
    run_pipeline()

    conn = sqlite3.connect("database.sqlite")
    df = pd.read_sql("SELECT * FROM historico", conn)
    conn.close()

    assert not df.empty, " O banco foi criado, mas está vazio!"
    print("✔ Teste OK — Banco populado com sucesso")
