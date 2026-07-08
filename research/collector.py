"""
CSV Collector
Production v1
"""

from pathlib import Path

import pandas as pd


class ProductCollector:

    def __init__(self):

        self.supported_name_columns = [

            "Product Name",
            "product_name",
            "Product",
            "Name",
            "Title"

        ]

        self.supported_price_columns = [

            "Price",
            "price",
            "Selling Price",
            "Sale Price"

        ]

        self.supported_category_columns = [

            "Category",
            "category"

        ]

        self.supported_image_columns = [

            "Image",
            "image",
            "Image URL"

        ]

    def detect_column(self, df, columns):

        for column in columns:

            if column in df.columns:

                return column

        return None

    def load(self, csv_file):

        df = pd.read_csv(csv_file)

        name_col = self.detect_column(
            df,
            self.supported_name_columns
        )

        if not name_col:

            raise Exception(
                "Product Name column not found."
            )

        price_col = self.detect_column(
            df,
            self.supported_price_columns
        )

        category_col = self.detect_column(
            df,
            self.supported_category_columns
        )

        image_col = self.detect_column(
            df,
            self.supported_image_columns
        )

        products = []

        for _, row in df.iterrows():

            product = {

                "product_name": str(row[name_col]).strip(),

                "price": 0,

                "category": "",

                "image": ""

            }

            if price_col:

                try:

                    product["price"] = float(
                        row[price_col]
                    )

                except Exception:

                    product["price"] = 0

            if category_col:

                product["category"] = str(
                    row[category_col]
                )

            if image_col:

                product["image"] = str(
                    row[image_col]
                )

            products.append(product)

        return products