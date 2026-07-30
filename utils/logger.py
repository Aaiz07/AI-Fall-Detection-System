"""
Logger Utility
--------------
Centralized logging for the AI Fall Detection System.

Responsibilities:
- Log information
- Log warnings
- Log errors
- Save logs to file
- Print logs to console
"""

import logging
import os
from datetime import datetime


class Logger:

    def __init__(self, log_dir="output/logs"):

        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(
            log_dir,
            f"system_{datetime.now().strftime('%Y%m%d')}.log"
        )

        self.logger = logging.getLogger("FallDetectionAI")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            # Console Output
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            # File Output
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)