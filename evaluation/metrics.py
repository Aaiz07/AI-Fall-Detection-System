"""
Evaluation Metrics
"""

import time


class EvaluationMetrics:

    def __init__(self):

        self.start_time = time.time()

        self.frames = 0
        self.people = 0

        self.tp = 0
        self.fp = 0
        self.fn = 0

        self.fps_values = []

    def update_frame(self, fps, people):

        self.frames += 1
        self.people += people
        self.fps_values.append(fps)

    def true_positive(self):

        self.tp += 1

    def false_positive(self):

        self.fp += 1

    def false_negative(self):

        self.fn += 1

    def precision(self):

        total = self.tp + self.fp

        if total == 0:
            return 0

        return self.tp / total

    def recall(self):

        total = self.tp + self.fn

        if total == 0:
            return 0

        return self.tp / total

    def f1_score(self):

        p = self.precision()
        r = self.recall()

        if p + r == 0:
            return 0

        return 2 * p * r / (p + r)

    def average_fps(self):

        if not self.fps_values:
            return 0

        return sum(self.fps_values) / len(self.fps_values)

    def summary(self):

        return {

            "frames": self.frames,

            "people": self.people,

            "tp": self.tp,

            "fp": self.fp,

            "fn": self.fn,

            "precision": round(
                self.precision(), 3
            ),

            "recall": round(
                self.recall(), 3
            ),

            "f1": round(
                self.f1_score(), 3
            ),

            "average_fps": round(
                self.average_fps(), 2
            )

        }