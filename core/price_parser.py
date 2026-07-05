import re


class PriceParser:

    @staticmethod
    def clean(price):

        if price is None:
            return None

        numbers = re.sub(r"[^\d]", "", str(price))

        if numbers == "":
            return None

        return int(numbers)