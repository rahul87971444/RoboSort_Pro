# 🤖 RoboSort Pro
## IoT-enabled robotic arm system capable of sorting multiple object categories with TFT display monitoring and web-based control dashboard.

<p align="center">
  <img src="images/setup.jpg" width="700">
</p>

<p align="center">
  <b>Machine Learning • Computer Vision • Robotics • IoT • Embedded Systems</b>
</p>

---

# 📖 Overview

RoboSort Pro is an intelligent robotic automation system designed to automatically identify, classify, and sort objects based on multiple parameters including:

- Shape
- Color
- Size
- Weight

The system combines **Machine Learning**, **Computer Vision**, **Weight Sensing**, **Robotic Manipulation**, **Embedded Systems**, and **Web-Based Monitoring** into a single smart automation platform.

Unlike traditional sorting systems that rely on a single parameter, RoboSort Pro performs multi-parameter classification and sorts objects into **16 unique categories** using a robotic arm.

The project was developed using a **Raspberry Pi 4B**, **TensorFlow Lite**, **OpenCV**, **Flask**, **HX711 Load Cell Module**, **TFT Display**, and a **6-DOF Robotic Arm**.

---

# 🚀 Key Features

## 🧠 Machine Learning Based Classification

- TensorFlow Lite image classification model
- Trained using Google Teachable Machine
- Edge AI inference on Raspberry Pi
- Real-time object recognition

---

## 👁️ Computer Vision

The system identifies:

### Shape

- Circle
- Rectangle

### Color

- Black
- White

### Size

- Small
- Large

using image classification and computer vision techniques.

---

## ⚖️ Weight-Based Classification

The system uses:

- Load Cell
- HX711 Amplifier Module

to measure object weight.

Weight categories:

- Light
- Heavy

---

## 🤖 Automated Robotic Arm Sorting

After classification:

- Object is picked automatically
- Target bin is determined
- Robotic arm places object into correct block
- Arm returns to home position

---

## 🌐 Flask Web Dashboard

The system includes a web dashboard with role-based access.

### 👨‍💼 Admin Dashboard

Features:

- Login Authentication
- Start System
- Stop System
- Reset Statistics
- Live Monitoring
- Object Count Statistics
- User Monitoring
- Sorting Logs

### 👀 Viewer Dashboard

Features:

- Read-Only Access
- Live Statistics
- Current Sorting Status
- System Monitoring

---

## 📺 TFT Display Integration

The TFT display provides:

- Object Prediction
- Confidence Score
- Weight Information
- Final Category
- Sorting Status

in real time.

---

# 🎯 Object Classification

The visual classifier predicts one of the following categories:

| ID | Category |
|----|----------|
| 0 | Black Small Circle |
| 1 | Black Big Circle |
| 2 | White Small Circle |
| 3 | White Big Circle |
| 4 | Black Small Rectangle |
| 5 | Black Big Rectangle |
| 6 | White Small Rectangle |
| 7 | White Big Rectangle |

---

# ⚙️ Final Sorting Categories

Visual classification is combined with weight classification to generate:

### Circle Objects

- Black Small Circle Light
- Black Small Circle Heavy
- Black Big Circle Light
- Black Big Circle Heavy

- White Small Circle Light
- White Small Circle Heavy
- White Big Circle Light
- White Big Circle Heavy

### Rectangle Objects

- Black Small Rectangle Light
- Black Small Rectangle Heavy
- Black Big Rectangle Light
- Black Big Rectangle Heavy

- White Small Rectangle Light
- White Small Rectangle Heavy
- White Big Rectangle Light
- White Big Rectangle Heavy

Total Categories: **16**

---

# 🏗️ System Architecture

```text
                     ┌─────────────────┐
                     │ Raspberry Pi 4B │
                     └────────┬────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
 Pi Camera Module       Load Cell + HX711      TFT Display
        │                     │
        └───────────┬─────────┘
                    ▼
          TensorFlow Lite Model
                    │
                    ▼
          Classification Engine
                    │
                    ▼
          Sorting Decision Logic
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 Flask Dashboard         PCA9685 Driver
                                │
                                ▼
                         6-DOF Robotic Arm
                                │
                                ▼
                           Sorted Bin
```

---

# 📸 Project Gallery

## Complete System

![System](images/setup.jpg)

---

## Robotic Arm

![Arm](images/robotic_arm.jpg)

---

## TFT Display

![TFT](images/tft_display.jpg)

---

## Admin Dashboard

![Admin](images/admin_dashboard.png)

---

## Viewer Dashboard

![Viewer](images/viewer_dashboard.png)

---

## Sorting Logs

![Logs](images/logs_dashboard.png)

---

# 🛠 Hardware Components

| Component | Quantity |
|------------|-----------|
| Raspberry Pi 4B (8GB) | 1 |
| Raspberry Pi Camera Module | 1 |
| 6-DOF Robotic Arm | 1 |
| PCA9685 Servo Driver | 1 |
| MG996R Servo Motors | 3 |
| SG90 Servo Motors | 3 |
| Load Cell | 1 |
| HX711 Amplifier | 1 |
| TFT Display | 1 |
| Buck Converter | 1 |
| Lithium-Ion Batteries | 3 |

---

# 💻 Software Stack

## Programming

- Python

## Machine Learning

- TensorFlow Lite
- Google Teachable Machine

## Computer Vision

- OpenCV
- Picamera2
- NumPy

## Web Development

- Flask
- HTML
- CSS
- JavaScript

## Embedded Systems

- Raspberry Pi GPIO
- PCA9685
- HX711

---

# 📂 Repository Structure

```text
RoboSort-Pro/
│
├── src/
│   ├── app.py
│   ├── dashboard_data.py
│   ├── display_manager.py
│   ├── main_controller.py
│   ├── ml_classifier.py
│   ├── servo_control.py
│   └── weight_sensor.py
│
├── templates/
│   ├── login.html
│   ├── admin_dashboard.html
│   ├── viewer_dashboard.html
│   └── logs.html
│
├── model/
│   ├── model_unquant.tflite
│   └── labels.txt
│
├── dataset/
│
├── data/
│   ├── robot_data.json
│   └── sorting_logs.txt
│
├── testing/
│
├── images/
│
├── videos/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 System Workflow

1. Object is placed on the platform.
2. Camera captures object image.
3. TensorFlow Lite model predicts visual category.
4. Load Cell measures object weight.
5. Weight category is assigned.
6. Final category is generated.
7. TFT display updates information.
8. Dashboard statistics are updated.
9. Sorting log is generated.
10. Robotic arm picks object.
11. Object is placed in assigned block.
12. Arm returns to home position.

---

# 📈 Future Enhancements

- Conveyor Belt Integration
- YOLO-Based Detection
- Cloud Dashboard
- Mobile Application
- MQTT Integration
- Industrial PLC Integration
- Voice Commands
- Predictive Analytics
- Advanced Deep Learning Models

---

# 🎓 Academic Significance

This project demonstrates practical integration of:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Robotics
- Embedded Systems
- IoT
- Human-Machine Interfaces
- Industrial Automation

within a single intelligent automation platform.

---

# 👥 Team

Developed as a collaborative B.Tech (CSE - IoT) engineering project focused on smart automation and intelligent object sorting.

---

# 📜 License

This project is released for educational and academic purposes.

MIT License

---

⭐ If you found this project useful, consider giving it a star.
