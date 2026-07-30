"""
===========================================
Ground Time Tracker
===========================================

Responsibilities
----------------
- Track how long a person stays on the ground
- Maintain timer for each tracked person
- Used to reduce false alarms

Author : FallDetectionAI
"""

import time


class GroundTime:

    def __init__(self):

        self.start_time = {}

    def update(self, track_id, on_ground):

        """
        Parameters
        ----------
        track_id : int
            ByteTrack ID

        on_ground : bool
            True if person is considered on the ground

        Returns
        -------
        float
            Time (seconds) spent on the ground
        """

        current_time = time.time()

        if on_ground:

            if track_id not in self.start_time:

                self.start_time[track_id] = current_time

            return current_time - self.start_time[track_id]

        else:

            if track_id in self.start_time:

                del self.start_time[track_id]

            return 0.0