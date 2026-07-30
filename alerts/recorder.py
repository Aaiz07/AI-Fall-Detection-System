"""
====================================================
Evidence Recorder
====================================================

Responsibilities
----------------
- Save fall snapshots
- Save evidence videos
- Maintain rolling frame buffer
- Record before & after a fall

Author : FallDetectionAI
"""

import os
import cv2
import time
from collections import deque


class EvidenceRecorder:

    def __init__(self):

        # Create output folder
        os.makedirs("output/evidence", exist_ok=True)

        # Video Settings
        self.fps = 30
        self.pre_event_seconds = 5
        self.post_event_seconds = 5

        # Store previous frames
        self.frame_buffer = deque(
            maxlen=self.fps * self.pre_event_seconds
        )

        # Recording State
        self.recording = False
        self.video_writer = None
        self.remaining_frames = 0

        print("[INFO] Evidence Recorder Initialized.")

    # --------------------------------------------------
    # Update every frame
    # --------------------------------------------------

    def update(self, frame):

        self.frame_buffer.append(frame.copy())

        if self.recording:

            self.video_writer.write(frame)

            self.remaining_frames -= 1

            if self.remaining_frames <= 0:

                self.stop_recording()

    # --------------------------------------------------
    # Save Snapshot
    # --------------------------------------------------

    def save_snapshot(self, frame, event):

        timestamp = int(time.time())

        filename = os.path.join(
            "output",
            "evidence",
            f"fall_{timestamp}.jpg"
        )

        cv2.imwrite(filename, frame)

        print(f"[INFO] Snapshot Saved : {filename}")

    # --------------------------------------------------
    # Start Video Recording
    # --------------------------------------------------

    def save_video(self, frame, event):

        if self.recording:
            return

        height, width = frame.shape[:2]

        timestamp = int(time.time())

        filename = os.path.join(
            "output",
            "evidence",
            f"fall_{timestamp}.mp4"
        )

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        self.video_writer = cv2.VideoWriter(
            filename,
            fourcc,
            self.fps,
            (width, height)
        )

        # Write buffered frames (before fall)

        for buffered_frame in self.frame_buffer:

            self.video_writer.write(buffered_frame)

        # Continue recording

        self.remaining_frames = (
            self.post_event_seconds * self.fps
        )

        self.recording = True

        print(f"[INFO] Recording Started : {filename}")

    # --------------------------------------------------
    # Stop Recording
    # --------------------------------------------------

    def stop_recording(self):

        if self.video_writer is not None:

            self.video_writer.release()

            self.video_writer = None

        self.recording = False

        self.remaining_frames = 0

        print("[INFO] Recording Completed.")

    # --------------------------------------------------
    # Cleanup
    # --------------------------------------------------

    def release(self):

        if self.video_writer is not None:

            self.video_writer.release()

            self.video_writer = None

        self.recording = False

        print("[INFO] Evidence Recorder Released.")