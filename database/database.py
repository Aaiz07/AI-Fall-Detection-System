"""
SQLite Database Manager
"""

import sqlite3
from datetime import datetime


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "fall_detection.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fall_events(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            track_id INTEGER,

            state TEXT,

            confidence REAL,

            body_angle REAL,

            velocity REAL,

            ground_time REAL,

            aspect_ratio REAL

        )
        """)

        self.connection.commit()

    def insert_event(self, event):

        f = event["features"]

        self.cursor.execute("""

        INSERT INTO fall_events(

            timestamp,
            track_id,
            state,
            confidence,
            body_angle,
            velocity,
            ground_time,
            aspect_ratio

        )

        VALUES(?,?,?,?,?,?,?,?)

        """,

        (

            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            event["track_id"],

            event["state"],

            event["confidence"],

            f["body_angle"],

            f["velocity"],

            f["ground_time"],

            f["aspect_ratio"]

        ))

        self.connection.commit()

    def close(self):

        self.connection.close()