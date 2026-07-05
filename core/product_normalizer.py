import re


class ProductNormalizer:

    REMOVE_WORDS = {

        "original",
        "official",
        "best",
        "new",
        "latest",
        "premium",
        "portable",
        "rechargeable",
        "wireless",
        "multifunctional",
        "high",
        "quality",
        "heavy",
        "duty",
        "stainless",
        "steel",
        "electric",
        "powerful",
        "machine",
        "kitchen",
        "tool",
        "tools",
        "germany",
        "japan",
        "technology"

    }

    @classmethod
    def normalize(cls, title):

        title = title.lower()

        title = re.sub(r"\([^)]*\)", " ", title)

        title = re.sub(r"\[[^\]]*\]", " ", title)

        title = re.sub(r"\d+\s?(ml|w|kw|v|pcs|pc|cm|mm)", " ", title)

        title = re.sub(r"[^a-z0-9 ]", " ", title)

        words = []

        for word in title.split():

            if len(word) <= 2:
                continue

            if word.isdigit():
                continue

            if word in cls.REMOVE_WORDS:
                continue

            words.append(word)

        return " ".join(words).strip()