import pandas as pd
import csv
import re
from langchain_core.documents import Document

CSV_PATH = "data/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv"

def convert_reviews_to_documents():
    try:
        df = pd.read_csv(
            CSV_PATH,
            encoding='utf-8',
            quoting=csv.QUOTE_MINIMAL,
            on_bad_lines='skip'
        )
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

    if not {'name', 'reviews.text'}.issubset(df.columns):
        print("Required columns missing")
        return []

    df = df[['name', 'reviews.text']].dropna()
    df['reviews.text'] = df['reviews.text'].astype(str).str.strip()
    df = df[df['reviews.text'] != '']

    docs = []
    for _, row in df.iterrows():
        page_content = re.sub(r'[^\x00-\x7F]+', '', row['reviews.text'])
        doc = Document(page_content=page_content, metadata={"product_name": row['name']})
        docs.append(doc)

    print(f"Converted {len(docs)} reviews into documents.")
    return docs
