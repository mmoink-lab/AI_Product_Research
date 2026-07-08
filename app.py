"""
BD Product Intelligence
Production App v1
"""

from pathlib import Path

import pandas as pd

from research.product_research_engine import ProductResearchEngine


INPUT_DIR = Path("data/input")
OUTPUT_DIR = Path("data/output")


def find_csv():

    csv_files = list(INPUT_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV found inside: {INPUT_DIR}"
        )

    return csv_files[0]


def detect_name_column(df):

    possible = [

        "Product Name",
        "product_name",
        "Product",
        "product",
        "Name",
        "name",
        "Title",
        "title"

    ]

    for col in possible:

        if col in df.columns:
            return col

    raise Exception("Product Name column not found.")


def detect_price_column(df):

    possible = [

        "Price",
        "price",
        "Selling Price",
        "selling_price",
        "Sale Price",
        "sale_price"

    ]

    for col in possible:

        if col in df.columns:
            return col

    return None


def load_products(csv_file):

    df = pd.read_csv(csv_file)

    name_col = detect_name_column(df)

    price_col = detect_price_column(df)

    products = []

    for _, row in df.iterrows():

        name = str(row[name_col]).strip()

        if not name:
            continue

        price = 0

        if price_col:

            try:
                price = float(row[price_col])
            except Exception:
                price = 0

        products.append({

            "product_name": name,

            "price": price

        })

    return products


def save_report(results):

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    out = OUTPUT_DIR / "winner_products.csv"

    pd.DataFrame(results).to_csv(
        out,
        index=False,
        encoding="utf-8-sig"
    )

    return out


def main():

    print("=" * 70)
    print("BD PRODUCT INTELLIGENCE")
    print("=" * 70)

    csv_file = find_csv()

    print("Input :", csv_file)

    products = load_products(csv_file)

    print("Products Loaded :", len(products))

    engine = ProductResearchEngine()

    results = engine.top_winners(products)

    output = save_report(results)

    print()

    print("Top 10 Products")

    print("-" * 70)

    for i, item in enumerate(results[:10], start=1):

        print(
            f"{i:02d}. "
            f"{item['product_name'][:55]:55} "
            f"{item['winner_score']}"
        )

    print("-" * 70)

    print("Report Saved :", output)

    print("=" * 70)


if __name__ == "__main__":

    main()