import pandas as pd


class ProductDeduplicator:
    """
    Remove duplicate products based on product name.
    """

    @staticmethod
    def remove_duplicates(
        df: pd.DataFrame,
        column: str = "Product"
    ) -> pd.DataFrame:

        if column not in df.columns:
            raise ValueError(
                f"Column '{column}' not found."
            )

        return (
            df.drop_duplicates(
                subset=[column],
                keep="first"
            )
            .reset_index(drop=True)
        )