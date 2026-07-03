# 🚗 Drunk Pattern Detection System

A real-time computer vision application that detects potential drunk behavior by analyzing facial presence and body posture using OpenCV and MediaPipe.

## 📌 Project Overview

This project uses a webcam to detect possible drunk behavior by combining face detection and body posture analysis.

### Features

- Real-time webcam monitoring
- Face detection using OpenCV
- Body posture detection using MediaPipe
- Live drunk/not drunk status
- Simple graphical user interface (GUI)

## 🛠 Technologies Used

- Python
- OpenCV
- MediaPipe
- Tkinter
- Pillow (PIL)

## 📂 Project Structure

```
Drunk-and-detection/
│
├── drunk and detection.py
├── README.md
├── requirements.txt
└── .gitignore
```

## ⚙ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶ Run the Project

```bash
python "drunk and detection.py"
```

## 🧠 Working

1. Captures live video from the webcam.
2. Detects the user's face using OpenCV.
3. Detects body posture using MediaPipe.
4. Checks shoulder movement.
5. Displays:

- 🟢 Not Drunk
- 🔴 Drunk

## 🚀 Future Improvements

- Eye Blink Detection
- Drowsiness Detection
- Head Pose Estimation
- Deep Learning Model
- Alert System

## 👩‍💻 Author

**Arna Gupta**

## 📄 License

This project is developed for educational purposes.