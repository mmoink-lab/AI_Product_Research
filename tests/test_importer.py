from pathlib import Path

from database.importer import ProductImporter

csv_file = Path("data/input/646.csv")

importer = ProductImporter()

total = importer.import_csv(csv_file)

print("=" * 80)

print("Imported :", total)

print()

products = importer.get_products()

print(products[:5])

print()

print("Database Total :", len(products))

print("=" * 80)

importer.close()