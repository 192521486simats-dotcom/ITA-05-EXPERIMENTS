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

# Check if a file was selected
if not file_path:
    print("No image selected.")
    exit()

# Read the image
img = cv2.imread(file_path)

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image.")
    exit()

# Sharpening kernel
kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

# Apply the filter
sharpened = cv2.filter2D(img, -1, kernel)

# Save the output image
cv2.imwrite("Sharpened_Image.jpg", sharpened)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Sharpened image saved as 'Sharpened_Image.jpg'")
