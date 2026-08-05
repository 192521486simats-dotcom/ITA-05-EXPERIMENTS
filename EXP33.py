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

# Check if the user selected a file
if not file_path:
    print("No image selected.")
    exit()

# Read the image in grayscale
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image.")
    exit()

# Create a 3x3 kernel
kernel = np.ones((3, 3), np.uint8)

# Apply Morphological Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Save the output image
cv2.imwrite("Morphological_Gradient.jpg", gradient)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Morphological Gradient image saved as 'Morphological_Gradient.jpg'")
