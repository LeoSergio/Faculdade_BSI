import tabula
import pandas as pd
from pathlib import Path

def extract_pdf_to_dataframe(pdf_path: str) -> pd.DataFrame:
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"❌ Arquivo não encontrado: {pdf_path}")

    print("📄 Lendo PDF...")

    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

    if not tables:
        raise ValueError(" Nenhuma tabela detectada no PDF.")

    df = pd.concat(tables, ignore_index=True)
    print(" Extração concluída.")

    return df
