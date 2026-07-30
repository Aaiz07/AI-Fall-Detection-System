"""
====================================================
camera/stream.py
Production Camera Module
====================================================

Supports:
- Laptop Webcam
- USB Camera
- RTSP/IP Camera
"""

import cv2
import config


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(config.CAMERA_SOURCE)

        if not self.cap.isOpened():
            raise RuntimeError(
                f"Unable to open camera source: {config.CAMERA_SOURCE}"
            )

        # Camera Resolution
        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            config.FRAME_WIDTH
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            config.FRAME_HEIGHT
        )

        # Camera FPS (best effort)
        if hasattr(config, "MAX_FPS"):
            self.cap.set(
                cv2.CAP_PROP_FPS,
                config.MAX_FPS
            )

        # Reduce internal buffering for lower latency
        self.cap.set(
            cv2.CAP_PROP_BUFFERSIZE,
            1
        )

    def read(self):
        """
        Read a frame from the camera.
        Returns:
            (success, frame)
        """

        success, frame = self.cap.read()

        if not success or frame is None:
            return False, None

        return True, frame

    def is_opened(self):
        """
        Check if camera is opened.
        """

        return self.cap.isOpened()

    def get_width(self):
        """
        Return camera width.
        """

        return int(
            self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

    def get_height(self):
        """
        Return camera height.
        """

        return int(
            self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

    def get_fps(self):
        """
        Return camera FPS.
        """

        fps = self.cap.get(cv2.CAP_PROP_FPS)

        if fps <= 1:
            fps = 30

        return fps

    def release(self):
        """
        Release camera resources.
        """

        if self.cap is not None:
            self.cap.release()