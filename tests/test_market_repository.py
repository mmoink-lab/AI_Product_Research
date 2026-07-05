from research.market_research import MarketResearch
from database.market_repository import MarketRepository


def main():

    research = MarketResearch()

    print("Searching Bangladesh Market...")

    products = research.search("mini blender")

    research.close()

    repo = MarketRepository()

    repo.save_products(products)

    loaded = repo.load_products()

    print("Saved :", len(products))
    print("Loaded:", len(loaded))
    print()

    if loaded:

        print(loaded[0])


if __name__ == "__main__":

    main()