import sqlite3
import pandas as pd


class ProductImporter:
    """
    Import products into SQLite database.
    """

    def __init__(self, db_path="database/database.db"):
        self.db_path = db_path

    def import_products(self, df: pd.DataFrame):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        records = []

        for _, row in df.iterrows():

            records.append((
                row.get("Product", ""),
                row.get("Price", None),
                row.get("Category", ""),
                row.get("Image", ""),
                ""
            ))

        cursor.executemany("""
        INSERT INTO products
        (
            product_name,
            price,
            category,
            image,
            family
        )
        VALUES (?, ?, ?, ?, ?)
        """, records)

        conn.commit()
        conn.close()

        return len(records)