import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    print("🧼 Limpando dataframe...")

    # Remove colunas sem nome
    df.columns = [c if "Unnamed" not in c else f"col_{i}" for i, c in enumerate(df.columns)]

    # Remove linhas totalmente vazias
    df.dropna(how="all", inplace=True)

    # Strip whitespace
    df.columns = [c.strip() for c in df.columns]

    print("✔ Limpeza concluída.")
    return df
