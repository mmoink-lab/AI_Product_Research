import re


class SearchFilter:

    STOP_WORDS = {
        "for",
        "with",
        "and",
        "the",
        "of",
        "in",
        "on",
        "to",
        "best",
        "original",
        "new",
        "high",
        "quality"
    }

    @classmethod
    def clean(cls, text):

        text = text.lower()

        text = re.sub(r"[^a-z0-9 ]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @classmethod
    def filter_products(cls, keyword, products):

        keyword = cls.clean(keyword)

        keywords = [

            word

            for word in keyword.split()

            if len(word) >= 3 and word not in cls.STOP_WORDS

        ]

        filtered = []

        for item in products:

            title = cls.clean(

                item["product"]

            )

            score = 0

            # Exact phrase
            if keyword == title:

                score += 10

            elif keyword in title:

                score += 8

            # Keyword matching
            for word in keywords:

                if word in title:

                    score += 3

            # Bonus if most keywords exist
            matched = sum(

                1

                for word in keywords

                if word in title

            )

            if keywords:

                ratio = matched / len(keywords)

            else:

                ratio = 0

            if ratio >= 0.70:

                score += 4

            # Accept reasonable matches
            if score >= 6:

                filtered.append(item)

        return filtered