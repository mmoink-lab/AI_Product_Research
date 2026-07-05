class ColumnMapper:

    COLUMN_ALIASES = {

        "product_name": [
            "product",
            "product name",
            "title",
            "item",
            "item name",
            "name"
        ],

        "selling_price": [
            "price",
            "sale price",
            "selling price",
            "regular price"
        ],

        "category": [
            "category",
            "collection",
            "group"
        ],

        "image": [
            "image",
            "image url",
            "main image",
            "thumbnail"
        ]

    }

    @classmethod
    def detect(cls, dataframe):

        detected = {}

        columns = [c.lower().strip() for c in dataframe.columns]

        for standard_name, aliases in cls.COLUMN_ALIASES.items():

            for alias in aliases:

                if alias in columns:

                    detected[standard_name] = alias

                    break

        return detected