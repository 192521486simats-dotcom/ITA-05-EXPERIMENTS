import cv2
import tkinter as tk
from tkinter import filedialog

# Hide Tkinter window
root = tk.Tk()
root.withdraw()

# Select video file
file_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[
        ("Video Files", "*.mp4 *.avi *.mov *.mkv"),
        ("All Files", "*.*")
    ]
)

# Check if user selected a file
if not file_path:
    print("No video selected.")
    exit()

# Open video
cap = cv2.VideoCapture(file_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read all frames into a list
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play video in reverse
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)

    # Press 'q' to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
