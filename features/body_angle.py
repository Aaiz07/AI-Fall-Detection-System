"""
===========================================
Body Angle Calculator
===========================================
"""

import math


class BodyAngle:

    def calculate(self, joints):

        try:

            left_shoulder = joints["left_shoulder"]
            right_shoulder = joints["right_shoulder"]

            left_hip = joints["left_hip"]
            right_hip = joints["right_hip"]

            shoulder_center = (
                (left_shoulder[0] + right_shoulder[0]) / 2,
                (left_shoulder[1] + right_shoulder[1]) / 2,
            )

            hip_center = (
                (left_hip[0] + right_hip[0]) / 2,
                (left_hip[1] + right_hip[1]) / 2,
            )

            dx = shoulder_center[0] - hip_center[0]
            dy = shoulder_center[1] - hip_center[1]

            angle = abs(math.degrees(math.atan2(dy, dx)))

            return angle

        except Exception:

            return None