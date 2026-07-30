"""
ByteTrack Person Tracker
------------------------
Tracks detected persons across frames and assigns a
persistent Track ID to each individual.
"""

from ultralytics.trackers.byte_tracker import BYTETracker


class PersonTracker:
    """
    ByteTrack wrapper.

    Responsibilities:
    -----------------
    - Maintain person identities
    - Assign Track IDs
    - Handle lost/reappearing tracks
    """

    def __init__(self):

        self.tracker = BYTETracker(
            args={
                "track_thresh": 0.5,
                "track_buffer": 30,
                "match_thresh": 0.8,
                "mot20": False
            },
            frame_rate=30
        )

    def update(self, detections):
        """
        Update tracker.

        Parameters
        ----------
        detections

        Returns
        -------
        Active tracks
        """

        return self.tracker.update(
            detections,
            None,
            None
        )