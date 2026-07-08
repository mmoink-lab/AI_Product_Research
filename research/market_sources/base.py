"""
Base Marketplace Interface
"""


class MarketSource:

    name = "base"

    def search(self, product_name):

        raise NotImplementedError