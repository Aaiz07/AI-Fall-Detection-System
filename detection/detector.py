"""
====================================================
YOLO11 Person Detector with ByteTrack
====================================================

Responsibilities
----------------
- Load YOLO11 model
- Detect persons only
- Track persons using ByteTrack
- Return tracking results

Author : FallDetectionAI
"""

from ultralytics import YOLO

from config import (
    YOLO_MODEL,
    PERSON_CLASS,
    CONFIDENCE_THRESHOLD,
    TRACKER,
)


class Detector:
    """
    Production-ready YOLO11 detector with ByteTrack.
    """

    def __init__(self):
        print("=" * 50)
        print("[INFO] Loading YOLO11 Model...")
        print("=" * 50)

        self.model = YOLO(YOLO_MODEL)

        print("[INFO] YOLO11 Loaded Successfully.")
        print("=" * 50)

    def detect(self, frame):
        """
        Detect and track people in a frame.

        Parameters
        ----------
        frame : numpy.ndarray
            Input image/frame

        Returns
        -------
        list
            Ultralytics Results object
        """

        results = self.model.track(
            source=frame,
            classes=[PERSON_CLASS],
            conf=CONFIDENCE_THRESHOLD,
            tracker=TRACKER,
            persist=True,
            verbose=False,
        )

        return results