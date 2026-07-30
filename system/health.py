"""
System Health Monitor
"""

import os
import shutil
import time

import psutil


class SystemHealth:

    def __init__(self):

        self.start = time.time()

    def get_status(
        self,
        fps,
        camera=True,
        database=True,
        detector=True,
        pose=True
    ):

        cpu = psutil.cpu_percent()

        memory = psutil.virtual_memory().percent

        disk = shutil.disk_usage(os.getcwd())

        uptime = int(time.time() - self.start)

        hours = uptime // 3600
        minutes = (uptime % 3600) // 60
        seconds = uptime % 60

        return {

            "camera": camera,

            "database": database,

            "detector": detector,

            "pose": pose,

            "fps": round(fps, 2),

            "cpu": cpu,

            "memory": memory,

            "disk_free": round(
                disk.free / (1024 ** 3),
                1
            ),

            "uptime":
                f"{hours:02}:{minutes:02}:{seconds:02}"

        }