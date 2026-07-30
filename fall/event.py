"""
====================================================
Fall Event
====================================================

Responsibilities
----------------
- Create standardized fall events
- Add timestamp
- Package detection results
- Used by alerts, recorder and dashboard

Author : FallDetectionAI
"""

from datetime import datetime


class FallEvent:

    def create(self, detection):

        event = {

            "state": detection["state"],

            "track_id": detection["track_id"],

            "confidence": detection["confidence"],

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "features": detection["features"]
        }

        return event