# 🛡️ CADMS V2
## Computer-Aided Detection and Monitoring System

CADMS (Computer-Aided Detection and Monitoring System) is an AI-powered intelligent video surveillance platform designed for real-time multi-camera monitoring, behavior analysis, event management, and evidence collection.

The system combines **YOLO11**, **ByteTrack**, **OpenCV**, and **FastAPI** to detect security events, automatically capture evidence, log incidents, and provide a professional web-based surveillance dashboard.

---

# 🚀 Features

## AI Surveillance

- ✅ Multi-camera monitoring
- ✅ Real-time object detection (YOLO11)
- ✅ Multi-object tracking (ByteTrack)
- ✅ Zone-based Intrusion Detection
- ✅ Modular Behavior Manager Architecture
- 🔄 Loitering Detection (In Progress)
- 📌 Future AI Behaviors
  - Line Crossing
  - Crowd Detection
  - Fall Detection
  - Abandoned Object Detection
  - Face Recognition

---

## Event Management

- Automatic intrusion detection
- Event generation
- Person ID tracking
- Evidence snapshot capture
- CSV event logging
- Timestamp recording
- Camera-wise event management

---

## Evidence Management

Automatically stores evidence in:

```
evidence/
    YYYY-MM-DD/
        CAMERA_NAME/
            HH-MM-SS_Person-001.jpg
```

Each event contains:

- Date
- Time
- Camera
- Event Type
- Person ID
- Evidence Path

---

# 🌐 Surveillance Dashboard

Built using:

- FastAPI
- HTML
- CSS
- JavaScript

Current Dashboard Features

- ✅ Live Event Table
- ✅ Live Statistics
- ✅ Search Events
- ✅ Camera Filter
- ✅ Event Filter
- ✅ Evidence Viewer
- ✅ Auto Refresh
- ✅ System Health Monitoring
- ✅ Online / Offline Status
- ✅ Live Date & Time

---

# 🏗️ System Architecture

```
                   Cameras
                      │
                      ▼
               Frame Buffer
                      │
                      ▼
               YOLO11 Detection
                      │
                      ▼
              ByteTrack Tracking
                      │
                      ▼
             Behavior Manager
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 Intrusion Detector         Future Behaviors
                             (Loitering,
                           Line Crossing,
                             Crowd, etc.)
                      │
                      ▼
               Event Manager
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Evidence Manager          Event Logger
        │                           │
        └─────────────┬─────────────┘
                      ▼
               FastAPI Backend
                      │
                      ▼
            Surveillance Dashboard
```

---

# 📂 Project Structure

```
CADMS_V2/

├── ai/
│   ├── v2/
│
├── backend/
│   ├── static/
│   ├── templates/
│   ├── services.py
│   ├── routes.py
│   └── app.py
│
├── behavior/
│   ├── behavior_manager.py
│   └── intrusion.py
│
├── cameras/
│
├── evidence/
│
├── events/
│   ├── event_manager.py
│   └── event_logger.py
│
├── logs/
│   └── events.csv
│
├── renderer/
│
├── system/
│   ├── system_health.py
│   └── health.json
│
├── main.py
├── config.py
└── requirements.txt
```

---

# ⚙️ Technologies Used

- Python 3.12
- OpenCV
- YOLO11 (Ultralytics)
- ByteTrack
- FastAPI
- Jinja2
- HTML
- CSS
- JavaScript
- CSV Logging
- JSON
- NumPy

---

# 📸 Event Flow

```
Person enters restricted zone
            │
            ▼
    Intrusion Detected
            │
            ▼
 Event Manager Triggered
            │
            ▼
 Snapshot Saved
            │
            ▼
 Event Logged (CSV)
            │
            ▼
 Dashboard Updated
```

---

# 📊 Current Development Status

## ✅ Completed

- Multi-camera architecture
- YOLO11 integration
- ByteTrack integration
- Intrusion Detection
- Evidence Manager
- Event Manager
- Event Logger
- CSV Logging
- FastAPI Backend
- Surveillance Dashboard
- Evidence Viewer
- Dashboard Statistics
- Search & Filters
- Live System Status
- Behavior Manager Architecture

---

## 🔄 Currently Working On

- Loitering Detection

---

## 📌 Planned Features

### AI Behaviors

- Line Crossing
- Crowd Detection
- Fall Detection
- Abandoned Object
- Face Recognition
- Vehicle Detection

### Dashboard

- Live Camera Grid
- Camera Health Monitoring
- Real-time Notifications
- Analytics Charts
- Evidence Gallery
- Recording Playback

### System

- User Authentication
- Role-based Access
- Report Generation
- AI Configuration Panel
- GPU Monitoring
- Recording Management

---

# 🛣️ Development Roadmap

| Phase | Status |
|--------|--------|
| Foundation Architecture | ✅ |
| Multi-Camera System | ✅ |
| YOLO11 Detection | ✅ |
| ByteTrack Tracking | ✅ |
| Intrusion Detection | ✅ |
| Evidence Management | ✅ |
| Dashboard V1 | ✅ |
| Behavior Manager | ✅ |
| Loitering Detection | 🔄 |
| Line Crossing | ⏳ |
| Crowd Detection | ⏳ |
| Fall Detection | ⏳ |
| Face Recognition | ⏳ |

---

# ▶️ Running the Project

Clone the repository

```bash
git clone https://github.com/swaudhin/CADMS_V2.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the AI Engine

```bash
py main.py
```

Run the Dashboard

```bash
py -m uvicorn backend.app:app --reload
```

Open

```
http://127.0.0.1:8000/dashboard
```

---

# 🎯 Project Objective

The goal of CADMS is to build a scalable AI-powered Video Management System (VMS) capable of:

- Real-time surveillance
- Intelligent behavior analysis
- Automated evidence collection
- Event monitoring
- Security analytics
- Professional monitoring dashboard

---

# 👨‍💻 Developer

**Swaudhin**

AI & Computer Vision Developer

GitHub:
https://github.com/swaudhin

---

# ⭐ Future Vision

CADMS is being developed as a professional AI Surveillance Platform capable of supporting multiple intelligent security analytics similar to commercial Video Management Systems (VMS).

Future versions will include advanced behavior analysis, live camera streaming, intelligent search, reporting, and enterprise-level surveillance capabilities.

---

**CADMS V2 — Intelligent AI Surveillance Platform**
