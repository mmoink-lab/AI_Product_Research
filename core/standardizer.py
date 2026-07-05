import re


class DataStandardizer:
    """
    Standardize product data before importing.
    """

    @staticmethod
    def clean_text(text):

        if text is None:
            return ""

        text = str(text).strip()

        text = re.sub(r"\s+", " ", text)

        return text.title()

    @staticmethod
    def clean_price(price):

        if price is None:
            return None

        price = str(price)

        price = price.replace("?", "")
        price = price.replace(",", "")
        price = price.replace("Tk", "")
        price = price.replace("tk", "")

        price = price.strip()

        try:
            return float(price)
        except ValueError:
            return None