from ultralytics import YOLO
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp")]
)

if image_path == "":
    print("No image selected.")
    exit()

model = YOLO("yolov8n.pt")

results = model(image_path)

img = results[0].plot()
