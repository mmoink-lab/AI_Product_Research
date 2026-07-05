from rapidfuzz import fuzz


class SimilarityEngine:

    def score(self, search_keyword, product_name):

        keyword = search_keyword.lower().strip()
        product = product_name.lower().strip()

        ratio = fuzz.token_set_ratio(keyword, product)

        return round(ratio, 2)