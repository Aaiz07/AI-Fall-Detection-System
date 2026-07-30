"""
====================================================
YOLO11 Pose Estimator
====================================================

Responsibilities
----------------
- Load YOLO11 Pose model once
- Perform pose estimation
- Return pose results

Author : FallDetectionAI
"""

from ultralytics import YOLO

from config import (
    POSE_MODEL,
    POSE_CONFIDENCE,
)


class PoseEstimator:

    def __init__(self):

        print("[INFO] Loading YOLO11 Pose Model...")

        self.model = YOLO(POSE_MODEL)

        print("[INFO] YOLO11 Pose Model Loaded Successfully.")

    def estimate(self, frame):

        results = self.model.predict(
            source=frame,
            conf=POSE_CONFIDENCE,
            verbose=False
        )

        return results