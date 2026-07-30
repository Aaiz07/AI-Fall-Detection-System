"""
===========================================
Hip Velocity Calculator
===========================================

Responsibilities
----------------
- Calculate vertical hip velocity
- Maintain previous hip position
- Used for fall detection

Author : FallDetectionAI
"""


class Velocity:

    def __init__(self):

        self.previous_y = {}
        self.previous_time = {}

    def calculate(self, track_id, hip_y, current_time):

        """
        Calculate vertical velocity (pixels/second)

        Returns
        -------
        float
            Positive = moving downward
            Negative = moving upward
        """

        if track_id not in self.previous_y:

            self.previous_y[track_id] = hip_y
            self.previous_time[track_id] = current_time

            return 0.0

        delta_y = hip_y - self.previous_y[track_id]

        delta_time = current_time - self.previous_time[track_id]

        if delta_time <= 0:

            return 0.0

        velocity = delta_y / delta_time

        self.previous_y[track_id] = hip_y
        self.previous_time[track_id] = current_time

        return velocity