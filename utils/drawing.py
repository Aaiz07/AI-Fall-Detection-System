"""
Drawing Utilities
-----------------
Handles all visualization for the AI Fall Detection System.

Responsibilities:
- Draw bounding boxes
- Draw Track IDs
- Draw confidence scores
- Draw FPS
- Draw status messages

Future Support:
- Pose Skeleton
- Fall Alert
- Person Counter
- Safe Zone
"""

import cv2

from config import (
    BOX_COLOR,
    TEXT_COLOR,
    FPS_COLOR,
    SHOW_TRACK_ID,
    SHOW_CONFIDENCE,
)


class Drawer:

    def __init__(self):
        pass

    def draw_detection(
    self,
    frame,
    x1,
    y1,
    x2,
    y2,
    confidence,
    track_id=None,
    status="NORMAL",
):
        """
        Draw one detected person.
        """

        cv2.rectangle(
            frame,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            BOX_COLOR,
            2,
        )

        label = ""

        if SHOW_TRACK_ID and track_id is not None:
           label += f"ID:{track_id} "

        if SHOW_CONFIDENCE:
           label += f"{confidence:.2f} "

        label += f"[{status}]"

        cv2.putText(
            frame,
            label,
            (int(x1), int(y1) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            TEXT_COLOR,
            2,
        )

    def draw_fps(self, frame, fps):

        cv2.putText(
            frame,
            f"FPS : {fps:.2f}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            FPS_COLOR,
            2,
        )

    def draw_status(
        self,
        frame,
        text,
        color=(0, 255, 255),
    ):

        cv2.putText(
            frame,
            text,
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2,
        )

    def draw_line(
        self,
        frame,
        start,
        end,
        color=(255, 0, 0),
        thickness=2,
    ):

        cv2.line(
            frame,
            start,
            end,
            color,
            thickness,
        )

    def draw_circle(
        self,
        frame,
        center,
        radius=4,
        color=(0, 0, 255),
    ):

        cv2.circle(
            frame,
            center,
            radius,
            color,
            -1,
        )