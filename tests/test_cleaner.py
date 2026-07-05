import pandas as pd

from core.cleaner import ProductCleaner


data = {
    "Product": [
        "USB Mini Blender",
        None,
        "Vegetable Chopper",
        None
    ],
    "Price": [
        1200,
        None,
        850,
        None
    ]
}

df = pd.DataFrame(data)

print("Before Cleaning")
print(df)

print("-" * 40)

clean_df = ProductCleaner.remove_empty_rows(df)

print("After Cleaning")
print(clean_df)