"""
Temporal Fall Verification
"""

import time


class FallVerifier:

    def __init__(self, verify_time=1.5):

        self.verify_time = verify_time

        self.start_times = {}

    def verify(self, track_id, state):

        now = time.time()

        if state != "FALL_SUSPECTED":

            self.start_times.pop(track_id, None)

            return False

        if track_id not in self.start_times:

            self.start_times[track_id] = now

            return False

        elapsed = now - self.start_times[track_id]

        return elapsed >= self.verify_time

    def reset(self, track_id):

        self.start_times.pop(track_id, None)