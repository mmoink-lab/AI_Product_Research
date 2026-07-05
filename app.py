from database.init_db import initialize_database

from research.market_research import MarketResearch
from database.market_repository import MarketRepository

from core.search_filter import SearchFilter
from core.duplicate_remover import DuplicateRemover
from core.family_detector import ProductFamilyDetector

from intelligence.demand_engine import DemandEngine
from intelligence.competition_engine import CompetitionEngine
from intelligence.saturation_engine import SaturationEngine
from intelligence.evergreen_engine import EvergreenEngine
from intelligence.seasonal_engine import SeasonalEngine
from intelligence.final_ranking_engine import FinalRankingEngine
from intelligence.product_decision import ProductDecision


def main():

    print("=" * 60)
    print("BANGLADESH PRODUCT INTELLIGENCE")
    print("=" * 60)

    initialize_database()

    keyword = input("\nEnter Product Keyword : ").strip()

    if not keyword:

        print("Invalid Keyword")
        return

    print("\nSearching Bangladesh Market...\n")

    research = MarketResearch()

    try:

        products = research.search(keyword)

    finally:

        research.close()

    print(f"Products Found      : {len(products)}")

    if not products:

        print("No Products Found")
        return

    products = SearchFilter.filter_products(

        keyword,

        products

    )

    print(f"Relevant Products   : {len(products)}")

    if not products:

        print("No Relevant Products Found")
        return

    products = DuplicateRemover.remove(

        products

    )

    print(f"Unique Products     : {len(products)}")

    cleaned_products = []

    for item in products:

        family = ProductFamilyDetector.get_family_name(

            item["product"]

        )

        if family == "UNKNOWN":

            continue

        item["family"] = family

        cleaned_products.append(item)

    print(f"Recognized Products : {len(cleaned_products)}")

    if not cleaned_products:

        print("No Supported Product Family Found")
        return

    repo = MarketRepository()

    repo.save_products(cleaned_products)

    products = repo.load_products()

    demand_engine = DemandEngine()
    competition_engine = CompetitionEngine()
    saturation_engine = SaturationEngine()
    evergreen_engine = EvergreenEngine()
    seasonal_engine = SeasonalEngine()
    ranking_engine = FinalRankingEngine()
    decision_engine = ProductDecision()

    demand = {

        item["family"]: item

        for item in demand_engine.analyze(products)

    }

    competition = {

        item["family"]: item

        for item in competition_engine.analyze(products)

    }

    saturation = {

        item["family"]: item

        for item in saturation_engine.analyze(products)

    }

    families = {}

    for item in products:

        family = item["family"]

        if family not in families:

            families[family] = item

    rows = []

    for family in families:

        d = demand.get(family, {})

        c = competition.get(family, {})

        s = saturation.get(family, {})

        evergreen = evergreen_engine.calculate(

            family

        )

        seasonal = seasonal_engine.calculate(

            family

        )

        final_score = ranking_engine.calculate(

            d.get("demand", 0),

            c.get("competition_score", 0),

            s.get("saturation_score", 0),

            evergreen,

            seasonal

        )

        rows.append({

            "family": family,

            "listings": d.get("listings", 0),

            "sold": d.get("sold", 0),

            "demand": round(

                d.get("demand", 0),

                2

            ),

            "competition": c.get(

                "competition_score",

                0

            ),

            "saturation": s.get(

                "saturation_score",

                0

            ),

            "score": round(

                final_score,

                2

            ),

            "decision": decision_engine.get(

                final_score

            )

        })

    rows.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    print()

    print("=" * 110)
    print("FINAL MARKET REPORT")
    print("=" * 110)

    for row in rows:

        print(f"Family         : {row['family']}")
        print(f"Listings       : {row['listings']}")
        print(f"Total Sold     : {row['sold']}")
        print(f"Demand         : {row['demand']}")
        print(f"Competition    : {row['competition']}")
        print(f"Saturation     : {row['saturation']}")
        print(f"Final Score    : {row['score']}")
        print(f"Recommendation : {row['decision']}")
        print("-" * 110)


if __name__ == "__main__":

    main()