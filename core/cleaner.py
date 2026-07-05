import pandas as pd


class ProductCleaner:
    """
    Clean and validate imported product data.
    """

    @staticmethod
    def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove completely empty rows.
        """
        return df.dropna(how="all").reset_index(drop=True)