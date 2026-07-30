"""
====================================================
Fall Detector
====================================================

Responsibilities
----------------
- Determine fall state
- Maintain person state
- Detect recovery
- Prevent false alarms

Author : FallDetectionAI
"""

from fall.confidence import ConfidenceEngine
from fall.recovery import RecoveryDetector


class FallDetector:

    def __init__(self):

        self.confidence_engine = ConfidenceEngine()
        self.recovery_detector = RecoveryDetector()

        # Current state of every tracked person
        self.person_state = {}

    def detect(self, features):

        track_id = features["track_id"]

        confidence = self.confidence_engine.calculate(features)

        previous_state = self.person_state.get(
            track_id,
            "NORMAL"
        )

        recovered = self.recovery_detector.update(
            track_id,
            features
        )

        # -----------------------------------
        # Recovery
        # -----------------------------------

        if previous_state == "FALL_DETECTED" and recovered:

            state = "RECOVERING"

        # -----------------------------------
        # Fall Detection
        # -----------------------------------

        elif confidence >= 80:

            state = "FALL_DETECTED"

        elif confidence >= 50:

            state = "FALL_SUSPECTED"

        else:

            # After recovery go back to NORMAL
            if previous_state == "RECOVERING":

                state = "NORMAL"

            else:

                state = "NORMAL"

        self.person_state[track_id] = state

        return {

            "track_id": track_id,

            "state": state,

            "confidence": confidence,

            "features": features

        }

    def reset(self, track_id):
        """
        Reset a person's state.
        """

        if track_id in self.person_state:
            del self.person_state[track_id]