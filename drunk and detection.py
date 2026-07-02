import cv2
import tkinter as tk
from PIL import Image, ImageTk
import mediapipe as mp

# Face Detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize Mediapipe Pose Detection
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Detect face to check if the person is in front of the camera
def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return len(faces) > 0

# Detect body posture to analyze drunk behavior
def detect_body(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)
    if results.pose_landmarks:
        nose_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
        left_shoulder_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        right_shoulder_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        # Check for swaying posture (Drunk sign)
        if abs(left_shoulder_y - right_shoulder_y) > 0.1:
            return True
    return False

# Main Detection Function
def detect_drunk(frame):
    face_detected = detect_face(frame)
    body_swaying = detect_body(frame)

    if face_detected and body_swaying:
        return True  # Drunk if both face and swaying body are detected
    return False

# Video Stream with GUI
def video_stream():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    root = tk.Tk()
    root.title("Drunk Pattern Detection")
    label = tk.Label(root)
    label.pack()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        is_drunk = detect_drunk(frame)
        status = "Drunk" if is_drunk else "Not drunk"
        color = (0, 0, 255) if is_drunk else (0, 255, 0)
        cv2.putText(frame, f"Status: {status}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb_frame)
        imgtk = ImageTk.PhotoImage(image=img)

        label.imgtk = imgtk
        label.configure(image=imgtk)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        root.update()

    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

if __name__ == "__main__":
    video_stream()