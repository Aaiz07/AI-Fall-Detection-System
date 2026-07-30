"""
====================================================
Detection ↔ Pose Matcher
====================================================

Responsibilities
----------------
- Match tracked detections with pose detections
- Uses IoU (Intersection over Union)
- Returns the correct pose for each Track ID

Author : FallDetectionAI
"""


class DetectionPoseMatcher:

    def __init__(self):
        pass

    def calculate_iou(self, boxA, boxB):
        """
        Calculate Intersection over Union (IoU)
        """

        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        inter_width = max(0, xB - xA)
        inter_height = max(0, yB - yA)

        inter_area = inter_width * inter_height

        if inter_area <= 0:
            return 0.0

        areaA = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
        areaB = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

        union = areaA + areaB - inter_area

        if union <= 0:
            return 0.0

        return inter_area / union

    def match(self, tracked_box, pose_persons):
        """
        Match one tracked person with one pose person.

        Parameters
        ----------
        tracked_box : list
            [x1, y1, x2, y2]

        pose_persons : list
            Output from KeypointExtractor

        Returns
        -------
        dict or None
        """

        best_person = None
        best_iou = 0.0

        for person in pose_persons:

            pose_box = person["bbox"]

            iou = self.calculate_iou(
                tracked_box,
                pose_box
            )

            if iou > best_iou:

                best_iou = iou
                best_person = person

        return best_person