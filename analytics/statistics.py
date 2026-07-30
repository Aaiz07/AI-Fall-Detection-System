"""
Live Analytics
"""

import time


class Statistics:

    def __init__(self):

        self.start_time = time.time()

        self.total_falls = 0
        self.total_recoveries = 0
        self.last_event = "None"

    def record_fall(self):

        self.total_falls += 1
        self.last_event = "FALL_DETECTED"

    def record_recovery(self):

        self.total_recoveries += 1
        self.last_event = "RECOVERING"

    def uptime(self):

        elapsed = int(time.time() - self.start_time)

        h = elapsed // 3600
        m = (elapsed % 3600) // 60
        s = elapsed % 60

        return f"{h:02}:{m:02}:{s:02}"

    def data(self, fps, active_people):

        return {

            "fps": round(fps, 2),

            "active_people": active_people,

            "falls": self.total_falls,

            "recoveries": self.total_recoveries,

            "last_event": self.last_event,

            "uptime": self.uptime()

        }