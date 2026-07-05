from intelligence.market_decision import MarketDecision

engine = MarketDecision()

scores = [95, 82, 71, 64, 58, 49, 30]

for score in scores:

    print(
        score,
        "->",
        engine.evaluate(score)
    )