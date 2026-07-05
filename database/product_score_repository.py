from database.db import get_connection


class ProductScoreRepository:

    def update_top_selling(self, family, score):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE products
            SET top_selling_score=?
            WHERE family=?
            """,
            (
                score,
                family
            )
        )

        conn.commit()
        conn.close()

    def update_evergreen(self, family, score):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE products
            SET evergreen_score=?
            WHERE family=?
            """,
            (
                score,
                family
            )
        )

        conn.commit()
        conn.close()

    def update_seasonal(self, family, score):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE products
            SET seasonal_score=?
            WHERE family=?
            """,
            (
                score,
                family
            )
        )

        conn.commit()
        conn.close()

    def update_opportunity(self, family, score):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE products
            SET opportunity_score=?
            WHERE family=?
            """,
            (
                score,
                family
            )
        )

        conn.commit()
        conn.close()

    def update_all_scores(

        self,
        family,
        top,
        evergreen,
        seasonal,
        opportunity

    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE products

            SET

            top_selling_score=?,
            evergreen_score=?,
            seasonal_score=?,
            opportunity_score=?

            WHERE family=?

            """,
            (
                top,
                evergreen,
                seasonal,
                opportunity,
                family
            )
        )

        conn.commit()
        conn.close()