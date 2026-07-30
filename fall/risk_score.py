"""
AI Fall Risk Score
"""


class FallRiskScore:

    def calculate(self, features):

        score = 0

        angle = features["body_angle"]
        velocity = features["velocity"]
        ground = features["ground_time"]
        aspect = features["aspect_ratio"]

        # Body angle contribution
        if angle < 20:
            score += 35
        elif angle < 35:
            score += 25
        elif angle < 50:
            score += 10

        # Velocity contribution
        if velocity > 400:
            score += 25
        elif velocity > 250:
            score += 15
        elif velocity > 100:
            score += 5

        # Ground time contribution
        if ground > 3:
            score += 25
        elif ground > 2:
            score += 15
        elif ground > 1:
            score += 5

        # Aspect ratio contribution
        if aspect > 1.5:
            score += 15
        elif aspect > 1.2:
            score += 10
        elif aspect > 1.0:
            score += 5

        return min(score, 100)