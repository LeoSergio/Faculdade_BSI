from extract.pdf_reader import extract_pdf_to_dataframe
from transform.clean_dataframe import clean_dataframe
from database.db_manage import save_to_database

PDF_PATH = "data/raw/historico.pdf"

def run_pipeline():
    print("\n=== PIPELINE INICIADO ===")

    df = extract_pdf_to_dataframe(PDF_PATH)
    df = clean_dataframe(df)

    print("\n Prévia do DataFrame:")
    print(df.head())

    save_to_database(df)

    print("\n=== PIPELINE FINALIZADO ===")

if __name__ == "__main__":
    run_pipeline()
