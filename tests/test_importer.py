import pandas as pd

from database.importer import ProductImporter

data = {
    "Product": [
        "USB Mini Blender",
        "Vegetable Chopper"
    ],
    "Price": [
        1200,
        850
    ],
    "Category": [
        "Kitchen",
        "Kitchen"
    ],
    "Image": [
        "img1.jpg",
        "img2.jpg"
    ]
}

df = pd.DataFrame(data)

importer = ProductImporter()

importer.import_products(df)

print("Import Successful")