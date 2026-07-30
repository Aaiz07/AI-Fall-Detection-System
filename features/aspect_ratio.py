"""
===========================================
Bounding Box Aspect Ratio
===========================================

Responsibilities
----------------
- Calculate width/height ratio
- Detect horizontal body posture
- Used as an additional fall indicator

Author : FallDetectionAI
"""


class AspectRatio:

    def calculate(self, x1, y1, x2, y2):

        """
        Calculate bounding box aspect ratio.

        Returns
        -------
        float
            width / height
        """

        width = abs(x2 - x1)
        height = abs(y2 - y1)

        if height == 0:
            return 0.0

        return width / height