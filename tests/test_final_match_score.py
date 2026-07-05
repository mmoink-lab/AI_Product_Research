from intelligence.final_match_score import FinalMatchScore

engine = FinalMatchScore()

score = engine.calculate(

    feature_score=75,

    name_score=83.78,

    position=0,

    total_results=20

)

print(score)