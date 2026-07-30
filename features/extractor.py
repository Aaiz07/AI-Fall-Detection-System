"""
====================================================
Feature Extraction Engine
====================================================

Responsibilities
----------------
- Calculate all fall detection features
- Provide a single interface
- Return structured feature dictionary

Author : FallDetectionAI
"""

from features.body_angle import BodyAngle
from features.hip_height import HipHeight
from features.velocity import Velocity
from features.ground_time import GroundTime
from features.aspect_ratio import AspectRatio


class FeatureExtractor:

    def __init__(self):

        self.body_angle = BodyAngle()
        self.hip_height = HipHeight()
        self.velocity = Velocity()
        self.ground_time = GroundTime()
        self.aspect_ratio = AspectRatio()

    def extract(
        self,
        joints,
        track_id,
        current_time,
        bbox
    ):
        """
        Parameters
        ----------
        joints : dict
            Pose keypoints

        track_id : int
            ByteTrack ID

        current_time : float
            Current timestamp

        bbox : tuple
            (x1, y1, x2, y2)

        Returns
        -------
        dict
            Extracted features
        """

        angle = self.body_angle.calculate(joints)

        hip = self.hip_height.calculate(joints)

        if hip is not None:
            hip_y = hip["y"]
        else:
            hip_y = None

        velocity = 0.0

        if hip_y is not None:

            velocity = self.velocity.calculate(
                track_id,
                hip_y,
                current_time
            )

        x1, y1, x2, y2 = bbox

        aspect_ratio = self.aspect_ratio.calculate(
            x1,
            y1,
            x2,
            y2
        )

        # Temporary logic
        # Will be replaced by the Fall Engine
        on_ground = False

        if angle is not None:

            if angle < 35 and aspect_ratio > 1.0:

                on_ground = True

        ground_time = self.ground_time.update(
            track_id,
            on_ground
        )

        return {

            "track_id": track_id,

            "body_angle": angle,

            "hip_height": hip,

            "velocity": velocity,

            "ground_time": ground_time,

            "aspect_ratio": aspect_ratio,

            "on_ground": on_ground,
        }