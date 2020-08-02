def calculateReqCalories(lbs, multiplier):
    kgs = int(round(int(lbs) / int(2.2), 2))
    RER = int(round(int(70) * int((kgs**0.75)), 2))
    MER = round(int(RER) * float(multiplier))
    return MER
