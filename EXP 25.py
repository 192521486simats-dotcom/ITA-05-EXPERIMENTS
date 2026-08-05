import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Hide the Tkinter window
root = tk.Tk()
root.withdraw()

# Open file dialog to select an image
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"),
        ("All Files", "*.*")
    ]
)

# Check if user selected an image
if not file_path:
    print("No image selected.")
    exit()

# Read the image
image = cv2.imread(file_path)

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute Sobel gradients
gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Subtract gradients
gradient = cv2.subtract(gradient_x, gradient_y)

# Convert to 8-bit image
gradient = cv2.convertScaleAbs(gradient)

# Save the output image
cv2.imwrite("sharpened_image3.jpg", gradient)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gradient Image", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Gradient image saved as 'sharpened_image3.jpg'")
