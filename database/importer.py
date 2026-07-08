"""
Database Importer
Production v1
"""

from database.repository import ProductRepository
from research.collector import ProductCollector


class ProductImporter:

    def __init__(self):

        self.collector = ProductCollector()
        self.repository = ProductRepository()

    def import_csv(self, csv_file):

        products = self.collector.load(csv_file)

        self.repository.clear()

        self.repository.insert_many(products)

        total = self.repository.total_products()

        return total

    def get_products(self):

        return self.repository.get_all()

    def close(self):

        self.repository.close()