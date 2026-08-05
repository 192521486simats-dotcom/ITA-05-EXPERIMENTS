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

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Morphological Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Save the output image
cv2.imwrite("Closing.jpg", closing)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Closing Image", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Closing image saved as 'Closing.jpg'")
