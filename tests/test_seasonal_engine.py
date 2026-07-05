from intelligence.seasonal_engine import SeasonalEngine

engine = SeasonalEngine()

families = [

    "Mini Blender",

    "Electric Grinder",

    "Umbrella",

    "Rain Coat"

]

for family in families:

    print(

        family,

        "->",

        engine.calculate(family)

    )