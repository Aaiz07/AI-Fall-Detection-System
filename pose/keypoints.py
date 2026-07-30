"""
====================================================
Pose Keypoint Extractor
====================================================

Responsibilities
----------------
- Extract 17 human body keypoints
- Extract pose bounding boxes
- Return structured pose information
- Used for Detection ↔ Pose matching

Author : FallDetectionAI
"""

import numpy as np


class KeypointExtractor:

    # COCO 17 Keypoints
    KEYPOINT_NAMES = [

        "nose",

        "left_eye",
        "right_eye",

        "left_ear",
        "right_ear",

        "left_shoulder",
        "right_shoulder",

        "left_elbow",
        "right_elbow",

        "left_wrist",
        "right_wrist",

        "left_hip",
        "right_hip",

        "left_knee",
        "right_knee",

        "left_ankle",
        "right_ankle",
    ]

    def extract(self, result):
        """
        Extract pose keypoints and bounding boxes.

        Parameters
        ----------
        result : ultralytics.engine.results.Results

        Returns
        -------
        list

        Example:

        [
            {
                "joints": {...},
                "bbox": [x1, y1, x2, y2]
            }
        ]
        """

        persons = []

        # No detections
        if result.keypoints is None:
            return persons

        if result.boxes is None:
            return persons

        # Pose keypoints
        keypoints = result.keypoints.xy.cpu().numpy()

        # Pose bounding boxes
        boxes = result.boxes.xyxy.cpu().numpy()

        # Iterate over each detected person
        for person_keypoints, person_box in zip(keypoints, boxes):

            joints = {}

            for index, (x, y) in enumerate(person_keypoints):

                joints[self.KEYPOINT_NAMES[index]] = (
                    float(x),
                    float(y)
                )

            persons.append({

                "joints": joints,

                "bbox": person_box.tolist()

            })

        return persons