from database.db import get_connection
from core.family_detector import ProductFamilyDetector


class MarketRepository:

    def save_products(self, products):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products")

        for item in products:

            family = item.get("family", "").strip()

            if not family:
                family = ProductFamilyDetector.get_family_name(
                    item.get("product", "")
                )

            cursor.execute(
                """
                INSERT INTO products(

                    product_name,
                    price,
                    sold_count,
                    category,
                    image,
                    family

                )

                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (

                    item.get("product", ""),
                    item.get("price", 0),
                    item.get("sold_count", 0),
                    item.get("category", ""),
                    item.get("image", ""),
                    family

                )
            )

        conn.commit()
        conn.close()

    def load_products(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT

                product_name,
                price,
                sold_count,
                category,
                image,
                family,
                top_selling_score,
                evergreen_score,
                seasonal_score,
                opportunity_score

            FROM products
            """
        )

        rows = cursor.fetchall()

        conn.close()

        products = []

        for row in rows:

            products.append({

                "product": row[0],
                "price": row[1],
                "sold_count": row[2],
                "category": row[3],
                "image": row[4],
                "family": row[5],
                "top_selling_score": row[6],
                "evergreen_score": row[7],
                "seasonal_score": row[8],
                "opportunity_score": row[9]

            })

        return products