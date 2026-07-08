"""
Marketplace Collector
"""

from research.market_sources.daraz import DarazProvider


class WebMarketCollector:

    def __init__(self):

        self.providers = []

        self.register(DarazProvider())

    def register(self, provider):

        self.providers.append(provider)

    def search(self, product_name):

        results = []

        for provider in self.providers:

            try:

                results.extend(
                    provider.search(product_name)
                )

            except Exception as e:
