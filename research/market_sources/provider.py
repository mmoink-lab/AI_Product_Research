"""
Marketplace Provider Base
"""

from abc import ABC, abstractmethod


class MarketplaceProvider(ABC):

    name = "Unknown"

    @abstractmethod
    def search(self, query: str):
        """
        Return list of normalized products.
        """
        pass

    def normalize(
        self,
        *,
        title="",
        price=0,
        seller="",
        url="",
        image="",
        marketplace=None,
    ):

        try:
            price = float(price)
        except Exception:
            price = 0

        return {
            "marketplace": marketplace or self.name,
            "title": title,
            "price": price,
            "seller": seller,
            "url": url,
            "image": image,
        }