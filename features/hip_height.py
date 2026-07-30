"""
===========================================
Hip Height Calculator
===========================================

Responsibilities
----------------
- Calculate hip center position
- Measure vertical hip location
- Used for fall detection

Author : FallDetectionAI
"""


class HipHeight:

    def calculate(self, joints):

        try:

            left_hip = joints["left_hip"]
            right_hip = joints["right_hip"]

            hip_center_x = (
                left_hip[0] + right_hip[0]
            ) / 2

            hip_center_y = (
                left_hip[1] + right_hip[1]
            ) / 2

            return {
                "x": hip_center_x,
                "y": hip_center_y
            }

        except Exception:

            return None