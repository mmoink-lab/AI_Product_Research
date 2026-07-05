from core.product_normalizer import ProductNormalizer


class DuplicateRemover:

    @classmethod
    def remove(cls, products):

        unique = {}

        for item in products:

            normalized = ProductNormalizer.normalize(

                item["product"]

            )

            if not normalized:

                continue

            item["normalized_name"] = normalized

            if normalized not in unique:

                unique[normalized] = item

                continue

            old = unique[normalized]

            if item["sold_count"] > old["sold_count"]:

                unique[normalized] = item

        return list(

            unique.values()

        )