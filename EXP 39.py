from ultralytics import YOLO
import cv2
import tkinter as tk
from tkinter import filedialog

# Hide Tkinter window
root = tk.Tk()
root.withdraw()

# Select video
video_path = filedialog.askopenfilename(
    title="Select Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
)

if not video_path:
    exit()

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture(video_path)

# Vehicle classes in COCO
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated = frame.copy()

    for box in results[0].boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        if label in vehicle_classes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(
                annotated,
                label,
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

    cv2.imshow("Vehicle Detection", annotated)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
