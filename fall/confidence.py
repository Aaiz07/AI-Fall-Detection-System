"""
====================================================
Fall Confidence Engine
====================================================

Responsibilities
----------------
- Calculate fall confidence score
- Combine multiple features
- Reduce false positives
- Return confidence between 0–100

Author : FallDetectionAI
"""


class ConfidenceEngine:

    def __init__(self):

        self.ANGLE_THRESHOLD = 35
        self.ASPECT_RATIO_THRESHOLD = 1.0
        self.VELOCITY_THRESHOLD = 300
        self.GROUND_TIME_THRESHOLD = 2

    def calculate(self, features):

        score = 0

        angle = features.get("body_angle")
        velocity = features.get("velocity", 0)
        ground_time = features.get("ground_time", 0)
        aspect_ratio = features.get("aspect_ratio", 0)

        # -----------------------------
        # Body Angle
        # -----------------------------
        if angle is not None and angle < self.ANGLE_THRESHOLD:
            score += 30

        # -----------------------------
        # Aspect Ratio
        # -----------------------------
        if aspect_ratio >= self.ASPECT_RATIO_THRESHOLD:
            score += 20

        # -----------------------------
        # Velocity
        # -----------------------------
        if velocity >= self.VELOCITY_THRESHOLD:
            score += 25

        # -----------------------------
        # Ground Time
        # -----------------------------
        if ground_time >= self.GROUND_TIME_THRESHOLD:
            score += 25

        return min(score, 100)