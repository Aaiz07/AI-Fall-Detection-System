"""
Production Decision Engine
"""


class DecisionEngine:

    def __init__(self):

        self.min_confidence = 80
        self.min_risk = 75

    def decide(
        self,
        confidence,
        risk_score,
        verified,
        recovered
    ):

        if recovered:
            return "RECOVERING"

        if verified:

            if confidence >= self.min_confidence:

                if risk_score >= self.min_risk:

                    return "FALL_DETECTED"

        if confidence >= 50:

            return "FALL_SUSPECTED"

        return "NORMAL"