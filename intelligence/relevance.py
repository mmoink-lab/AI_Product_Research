class RelevanceAnalyzer:

    def score(self, keyword, product_name):

        keyword_words = keyword.lower().split()
        product = product_name.lower()

        matched = 0

        for word in keyword_words:

            if word in product:
                matched += 1

        if len(keyword_words) == 0:
            return 0

        return round((matched / len(keyword_words)) * 100, 2)