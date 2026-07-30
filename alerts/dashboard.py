"""
====================================================
dashboard.py
Production Dashboard
====================================================
"""

import cv2


class Dashboard:

    def __init__(self):
        pass

    def draw(self, frame, detection, fps):

        state = detection.get("state", "NORMAL")
        confidence = detection.get("confidence", 0)
        track_id = detection.get("track_id", "N/A")

        if state == "FALL_DETECTED":
            color = (0, 0, 255)

        elif state == "FALL_SUSPECTED":
            color = (0, 165, 255)

        elif state == "RECOVERING":
            color = (0, 255, 255)

        else:
            color = (0, 255, 0)

        cv2.rectangle(
            frame,
            (10, 10),
            (340, 150),
            (40, 40, 40),
            -1
        )

        cv2.rectangle(
            frame,
            (10, 10),
            (340, 150),
            color,
            2
        )

        cv2.putText(
            frame,
            "AI FALL DETECTION",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"State : {state}",
            (20, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

        cv2.putText(
            frame,
            f"Confidence : {confidence:.1f}%",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Track ID : {track_id}",
            (20, 115),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"FPS : {fps:.1f}",
            (20, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

    def draw_statistics(self, frame, stats):

        x = 20
        y = 190

        cv2.rectangle(
            frame,
            (10, 165),
            (340, 355),
            (40, 40, 40),
            -1
        )

        cv2.rectangle(
            frame,
            (10, 165),
            (340, 355),
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "SYSTEM ANALYTICS",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        y += 35

        cv2.putText(
            frame,
            f"Active Persons : {stats['active_people']}",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

        y += 30

        cv2.putText(
            frame,
            f"Falls Detected : {stats['falls']}",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

        y += 30

        cv2.putText(
            frame,
            f"Recoveries : {stats['recoveries']}",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        y += 30

        cv2.putText(
            frame,
            f"Last Event : {stats['last_event']}",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        y += 30

        cv2.putText(
            frame,
            f"Uptime : {stats['uptime']}",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        y += 30

        cv2.putText(
            frame,
            f"FPS : {stats['fps']}",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2
        )