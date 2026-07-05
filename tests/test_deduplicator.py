import pandas as pd

from core.deduplicator import ProductDeduplicator

data = {
    "Product": [
        "USB Mini Blender",
        "Vegetable Chopper",
        "USB Mini Blender",
        "LED Strip Light"
    ],
    "Price": [
        1200,
        850,
        1250,
        450
    ]
}

df = pd.DataFrame(data)

print("Before")
print(df)

print("-" * 40)

clean_df = ProductDeduplicator.remove_duplicates(df)

print("After")
print(clean_df)