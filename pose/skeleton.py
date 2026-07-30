"""
====================================================
Pose Skeleton Drawer
====================================================

Responsibilities
----------------
- Draw human skeleton
- Draw body keypoints
- Keep visualization separate from AI inference

Author : FallDetectionAI
"""

import cv2

from config import (
    DRAW_KEYPOINTS,
    DRAW_SKELETON,
)


class SkeletonDrawer:

    # COCO skeleton connections
    CONNECTIONS = [

        # Face
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),

        # Arms
        (5, 6),
        (5, 7),
        (7, 9),
        (6, 8),
        (8, 10),

        # Body
        (5, 11),
        (6, 12),
        (11, 12),

        # Legs
        (11, 13),
        (13, 15),
        (12, 14),
        (14, 16),
    ]

    def draw(self, frame, result):

        if result.keypoints is None:
            return frame

        keypoints = result.keypoints.xy.cpu().numpy()

        for person in keypoints:

            # ---------------------------
            # Draw Skeleton
            # ---------------------------

            if DRAW_SKELETON:

                for start, end in self.CONNECTIONS:

                    x1, y1 = person[start]
                    x2, y2 = person[end]

                    if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:

                        cv2.line(
                            frame,
                            (int(x1), int(y1)),
                            (int(x2), int(y2)),
                            (0, 255, 0),
                            2,
                        )

            # ---------------------------
            # Draw Keypoints
            # ---------------------------

            if DRAW_KEYPOINTS:

                for x, y in person:

                    if x > 0 and y > 0:

                        cv2.circle(
                            frame,
                            (int(x), int(y)),
                            4,
                            (0, 0, 255),
                            -1,
                        )

        return frame