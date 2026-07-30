"""
config.py
AI Fall Detection Configuration
"""

# =====================================================
# CAMERA
# =====================================================

CAMERA_SOURCE =  "videos/test5.mp4"

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

MAX_FPS = 30

WINDOW_NAME = "AI Fall Detection"

POSE_SKIP_FRAMES = 12

# =====================================================
# DETECTION MODEL
# =====================================================

DETECTION_MODEL = "models/yolo11n.pt"

# Backward compatibility
YOLO_MODEL = DETECTION_MODEL

# =====================================================
# POSE MODEL
# =====================================================

POSE_MODEL = "models/yolo11n-pose.pt"

POSE_CONFIDENCE = 0.50

# =====================================================
# YOLO SETTINGS
# =====================================================

PERSON_CLASS = 0

CONFIDENCE_THRESHOLD = 0.35

IOU_THRESHOLD = 0.45

TRACKER = "bytetrack.yaml"

# =====================================================
# FALL DETECTION
# =====================================================

BODY_ANGLE_THRESHOLD = 55

ASPECT_RATIO_THRESHOLD = 1.20

HIP_HEIGHT_THRESHOLD = 0.30

VELOCITY_THRESHOLD = 1.0

GROUND_TIME_THRESHOLD = 1.5

FALL_CONFIRMATION_TIME = 1.5

# =====================================================
# RECORDING
# =====================================================

PRE_EVENT_SECONDS = 5

POST_EVENT_SECONDS = 10

OUTPUT_FOLDER = "output"

SNAPSHOT_FOLDER = "output/snapshots"

VIDEO_FOLDER = "output/videos"

# =====================================================
# DATABASE
# =====================================================

DATABASE_NAME = "fall_detection.db"

CSV_LOG_FILE = "logs/fall_events.csv"

# =====================================================
# ALERTS
# =====================================================

ENABLE_SOUND = True

ENABLE_POPUP = True

TELEGRAM_ENABLED = False

BOT_TOKEN = ""

CHAT_ID = ""

# =====================================================
# DISPLAY
# =====================================================

SHOW_FPS = True

SHOW_TRACK_ID = True

SHOW_CONFIDENCE = True

SHOW_ANALYTICS = True

SHOW_SKELETON = True

SHOW_BOUNDING_BOX = True

# =====================================================
# COLORS (BGR)
# =====================================================

COLOR_NORMAL = (0, 255, 0)

COLOR_SUSPECTED = (0, 255, 255)

COLOR_FALL = (0, 0, 255)

COLOR_RECOVERING = (255, 0, 0)

COLOR_TEXT = (255, 255, 255)

# =====================================================
# PERFORMANCE
# =====================================================

ENABLE_GPU = True

USE_HALF_PRECISION = False

# =====================================================
# LOGGING
# =====================================================

LOG_LEVEL = "INFO"

SAVE_LOGS = True

# =====================================================
# SYSTEM
# =====================================================

SYSTEM_NAME = "AI Fall Detection"

VERSION = "1.0.0"
# =====================================================
# POSE DRAWING SETTINGS
# =====================================================

DRAW_KEYPOINTS = True

DRAW_SKELETON = True

KEYPOINT_RADIUS = 4

KEYPOINT_THICKNESS = -1

SKELETON_THICKNESS = 2

KEYPOINT_COLOR = (0, 255, 255)

SKELETON_COLOR = (255, 0, 255)

# =====================================================
# POSE DRAWING
# =====================================================

DRAW_KEYPOINTS = True
DRAW_SKELETON = True

# =====================================================
# DRAWING CONFIGURATION
# =====================================================

BOX_COLOR = (0, 255, 0)

TEXT_COLOR = (255, 255, 255)

BOX_THICKNESS = 2

FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX

FONT_SCALE = 0.6

TEXT_THICKNESS = 2

# =====================================================
# DRAWING SETTINGS
# =====================================================

BOX_COLOR = (0, 255, 0)       # Green bounding box

TEXT_COLOR = (255, 255, 255)  # White text

FPS_COLOR = (0, 255, 255)     # Yellow FPS text
