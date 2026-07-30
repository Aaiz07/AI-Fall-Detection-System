"""
====================================================
Alert Notification System
====================================================

Responsibilities
----------------
- Send only ONE alert per fall
- Prevent duplicate alerts
- Reset after recovery

Author : FallDetectionAI
"""

import time


class AlertNotifier:

    def __init__(self):

        # Track IDs that have already triggered an alert
        self.active_alerts = {}

        # Minimum seconds before another alert
        self.cooldown = 10

    def notify(self, event):

        track_id = event["track_id"]

        current_time = time.time()

        # Already alerted?
        if track_id in self.active_alerts:

            last_time = self.active_alerts[track_id]

            if current_time - last_time < self.cooldown:
                return False

        self.active_alerts[track_id] = current_time

        print("\n" + "=" * 60)
        print("🚨 FALL DETECTED")
        print("=" * 60)
        print(f"Track ID   : {track_id}")
        print(f"Confidence : {event['confidence']:.1f}%")
        print(f"Time       : {event['timestamp']}")
        print("=" * 60 + "\n")

        return True

    def reset(self, track_id):
        """
        Allow future alerts after recovery.
        """

        if track_id in self.active_alerts:
            del self.active_alerts[track_id]