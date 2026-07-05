from intelligence.opportunity_engine import OpportunityEngine

engine = OpportunityEngine()

examples = [

    ("Mini Blender", 80.0, 1025),

    ("Electric Grinder", 20.0, 973),

]

for family, share, price in examples:

    score = engine.calculate(
        share,
        price
    )

    print(
        family,
        "|",
        score
    )