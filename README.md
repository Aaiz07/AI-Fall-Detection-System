# 🛡️ AI Fall Detection System

A real-time Human Fall Detection System developed using **YOLO11 Pose**, **OpenCV**, and **Python**. The system detects human falls, verifies the event, records evidence, and generates alerts while reducing false alarms through posture and motion analysis.

---

## 📌 Overview

Falls are one of the leading causes of serious injuries among elderly people and patients. This project aims to provide a real-time AI-powered monitoring system capable of detecting falls from live video streams or recorded videos.

The system combines person detection, pose estimation, feature extraction, temporal analysis, and event verification to improve reliability.

---

# 🚀 Features

- ✅ Real-time human detection
- ✅ YOLO11 Pose estimation
- ✅ Body posture analysis
- ✅ Human tracking
- ✅ Fall verification engine
- ✅ Confidence-based decision making
- ✅ Event logging
- ✅ Evidence image capture
- ✅ Video recording of detected falls
- ✅ Dashboard for monitoring
- ✅ SQLite database integration
- ✅ Performance evaluation module

---

# 🏗️ System Architecture

```
Camera / Video
        │
        ▼
YOLO11 Person Detection
        │
        ▼
YOLO11 Pose Estimation
        │
        ▼
Feature Extraction
        │
        ▼
Fall Verification
        │
        ▼
Decision Engine
        │
        ▼
Alert + Event Recording
        │
        ├── Evidence Image
        ├── Recorded Video
        └── Database Logging
```

---

# 🧠 Technologies Used

- Python
- OpenCV
- YOLO11
- Ultralytics
- NumPy
- SQLite
- Tkinter (GUI)
- Computer Vision
- Pose Estimation

---

# 📂 Project Structure

```
AI-Fall-Detection-System
│
├── alerts/
├── analytics/
├── camera/
├── database/
├── detection/
├── evaluation/
├── fall/
├── features/
├── gui/
├── models/
├── performance/
├── pose/
├── reports/
├── system/
├── test_videos/
├── utils/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

```bash
git clone https://github.com/Aaiz07/AI-Fall-Detection-System.git

cd AI-Fall-Detection-System

pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python app.py
```

---

# 📊 Current Capabilities

- Real-time monitoring
- Fall detection
- Event verification
- Evidence recording
- Alert generation
- Database logging

---

# 🔮 Future Improvements

- Activity Recognition (Walking, Sitting, Sleeping, Tying Shoes)
- Confidence Score Visualization
- Recovery Detection
- Multi-Person Fall Detection
- Explainable AI Dashboard
- Deep Learning Sequence Classifier
- Mobile Notifications
- Cloud Deployment

---

# 🎯 Applications

- Elderly Care
- Hospitals
- Smart Homes
- Assisted Living Facilities
- Industrial Safety
- Surveillance Systems

---

# 👨‍💻 Author

**Aaiz Tariq**

Data Science Intern

GitHub:
https://github.com/Aaiz07

---

## ⭐ If you find this project useful, consider giving it a Star.