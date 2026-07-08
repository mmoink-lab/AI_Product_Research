"""
Database Repository
Production v1
"""

import sqlite3
from pathlib import Path


class ProductRepository:

    def __init__(self, db_path="database/database.db"):

        self.db_path = Path(db_path)

        self.conn = sqlite3.connect(self.db_path)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

    def insert_product(self, product):

        self.cursor.execute(
            """
            INSERT INTO products
            (
                product_name,
                category,
                price,
                image,
                family
            )
            VALUES
            (?, ?, ?, ?, ?)
            """,
            (
                product.get("product_name", ""),
                product.get("category", ""),
                product.get("price", 0),
                product.get("image", ""),
                product.get("family", "")
            )
        )

        self.conn.commit()

    def insert_many(self, products):

        data = []

        for product in products:

            data.append(

                (
                    product.get("product_name", ""),
                    product.get("category", ""),
                    product.get("price", 0),
                    product.get("image", ""),
                    product.get("family", "")
                )

            )

        self.cursor.executemany(

            """
            INSERT INTO products
            (
                product_name,
                category,
                price,
                image,
                family
            )
            VALUES
            (?, ?, ?, ?, ?)
            """,

            data

        )

        self.conn.commit()

    def get_all(self):

        self.cursor.execute(

            """
            SELECT *
            FROM products
            """
        )

        return [

            dict(row)

            for row in self.cursor.fetchall()

        ]

    def total_products(self):

        self.cursor.execute(

            """
            SELECT COUNT(*)
            FROM products
            """
        )

        return self.cursor.fetchone()[0]

    def clear(self):

        self.cursor.execute(

            """
            DELETE FROM products
            """
        )

        self.conn.commit()

    def close(self):

        self.conn.close()