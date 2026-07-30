"""
====================================================
Recovery Detection Engine
====================================================

Responsibilities
----------------
- Detect when a fallen person stands up again
- Prevent repeated fall alerts
- Reset person state

Author : FallDetectionAI
"""


class RecoveryDetector:

    def __init__(self):

        self.recovered = {}

    def update(self, track_id, features):

        angle = features.get("body_angle")
        aspect = features.get("aspect_ratio")
        ground_time = features.get("ground_time")

        if angle is None:
            return False

        # Person is upright again
        if (
            angle > 60
            and aspect < 0.8
            and ground_time < 1
        ):

            self.recovered[track_id] = True
            return True

        return False