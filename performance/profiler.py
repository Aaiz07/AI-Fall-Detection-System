"""
Performance Profiler
"""

import time


class PerformanceProfiler:

    def __init__(self):

        self.times = {}

    def start(self, name):

        self.times[name] = time.perf_counter()

    def stop(self, name):

        if name not in self.times:
            return 0.0

        elapsed = (
            time.perf_counter() -
            self.times[name]
        ) * 1000

        self.times[name] = elapsed

        return elapsed

    def summary(self):

        return {

            key: round(value, 2)

            for key, value in self.times.items()

            if isinstance(value, float)

        }
    
    