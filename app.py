"""
app.py - Production integration entry point
"""

import time
import cv2
import config

from camera.stream import Camera
from detection.detector import Detector
from pose.estimator import PoseEstimator
from pose.keypoints import KeypointExtractor
from pose.skeleton import SkeletonDrawer
from features.extractor import FeatureExtractor
from fall.detector import FallDetector
from fall.event import FallEvent
from alerts.notifier import AlertNotifier
from alerts.recorder import EvidenceRecorder
from alerts.dashboard import Dashboard
from utils.drawing import Drawer
from utils.logger import Logger
from utils.matcher import DetectionPoseMatcher
from logs.event_logger import EventLogger
from fall.verifier import FallVerifier
from database.database import DatabaseManager
from analytics.statistics import Statistics
from alerts.telegram import TelegramAlert
from reports.report_generator import ReportGenerator
from gui.control_panel import ControlPanel
from recording.manager import RecordingManager
from fall.risk_score import FallRiskScore
from fall.decision_engine import DecisionEngine
from system.health import SystemHealth
from evaluation.metrics import EvaluationMetrics
from performance.profiler import PerformanceProfiler


verifier = FallVerifier()
database = DatabaseManager()
statistics = Statistics()
report_generator = ReportGenerator()
panel = ControlPanel()
video_manager = RecordingManager(fps=30)
risk_score = FallRiskScore()
decision_engine = DecisionEngine()
health = SystemHealth()
metrics = EvaluationMetrics()
profiler = PerformanceProfiler()


telegram = None
if config.TELEGRAM_ENABLED:
    telegram = TelegramAlert(
        config.BOT_TOKEN,
        config.CHAT_ID
    )


def main():

    logger = Logger()

    camera = Camera()
    detector = Detector()

    pose_estimator = PoseEstimator()
    keypoint_extractor = KeypointExtractor()
    skeleton_drawer = SkeletonDrawer()

    feature_extractor = FeatureExtractor()
    fall_detector = FallDetector()
    fall_event = FallEvent()

    notifier = AlertNotifier()
    recorder = EvidenceRecorder()
    event_logger = EventLogger()

    dashboard = Dashboard()
    drawer = Drawer()

    matcher = DetectionPoseMatcher()

    previous_time = time.time()

    frame_count = 0
    cached_pose_people = []

    while True:

        ok, frame = camera.read()

        if not ok:
            logger.error("Camera frame not available.")
            break

        recorder.update(frame)

        now = time.time()

        fps = 1.0 / max(now - previous_time, 1e-6)
        previous_time = now

        detections = detector.detect(frame)

        frame_count += 1

        if frame_count % config.POSE_SKIP_FRAMES == 0:

            poses = pose_estimator.estimate(frame)

            if poses:

                pose_result = poses[0]

                skeleton_drawer.draw(frame, pose_result)

                cached_pose_people = keypoint_extractor.extract(
                    pose_result
                )
            
        pose_people = cached_pose_people

        dashboard_result = {
            "state": "NORMAL",
            "confidence": 0,
            "track_id": "N/A"
        }

        if detections:

            boxes = detections[0].boxes

            if boxes is not None:

                for box in boxes:

                    x1, y1, x2, y2 = box.xyxy[0].tolist()

                    confidence = float(box.conf[0])

                    track_id = None

                    if box.id is not None:
                        track_id = int(box.id.item())

                    tracked_box = [x1, y1, x2, y2]

                    status = "NORMAL"

                    matched = matcher.match(
                        tracked_box,
                        pose_people
                    )

                    if matched and track_id is not None:

                        features = feature_extractor.extract(
                            joints=matched["joints"],
                            bbox=tracked_box,
                            track_id=track_id,
                            current_time=now,
                        )

                        result = fall_detector.detect(features)

                        status = result["state"]

                        dashboard_result = result

                        if status == "FALL_DETECTED":
                             if verifier.verify(track_id, status):
                                 result["state"] = "FALL_DETECTED"

                             event = fall_event.create(result)

                             notifier.notify(event)

                             recorder.save_snapshot(
                                frame,
                                event
                            )

                             recorder.save_video(
                                frame,
                                event
                            )

                             event_logger.log(event)
                             database.insert_event(event)

                        elif status == "RECOVERING":

                            notifier.reset(track_id)

                    drawer.draw_detection(
                        frame=frame,
                        x1=x1,
                        y1=y1,
                        x2=x2,
                        y2=y2,
                        confidence=confidence,
                        track_id=track_id,
                        status=status,
                    )

        dashboard.draw(
            frame,
            dashboard_result,
            fps
        )
        stats = statistics.data(
              fps=fps,
              active_people=len(boxes) if detections and boxes is not None else 0
        )
        dashboard.draw_statistics(frame, stats)


        cv2.imshow(
            "AI Fall Detection",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    recorder.release()
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    database.close()

