from ultralytics import YOLO
import cv2
import tkinter as tk
from tkinter import filedialog

# Hide Tkinter window
root = tk.Tk()
root.withdraw()

# Select image
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.jpeg")]
)

if not file_path:
    print("No image selected.")
    exit()

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Read image
img = cv2.imread(file_path)

# Detect objects
results = model(img)

# Draw boxes and labels
for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    cls = int(box.cls[0])
    conf = float(box.conf[0])

    label = model.names[cls]

    cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.putText(img,
                f"{label} {conf:.2f}",
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2)

    # Crop detected object
    obj = img[y1:y2, x1:x2]

    cv2.imwrite(f"{label}.jpg", obj)

    print("Detected:", label)

cv2.imshow("Detected Objects", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
