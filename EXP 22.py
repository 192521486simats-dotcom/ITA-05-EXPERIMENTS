import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Hide the Tkinter window
root = tk.Tk()
root.withdraw()

# Open file dialog
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

# Define the kernel
kernel = np.array([
    [0, 1, 0],
    [1, -8, 1],
    [0, 1, 0]
])

# Apply the filter
sharpened = cv2.filter2D(image, -1, kernel)

# Save the output image
cv2.imwrite("Sharpened.jpg", sharpened)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Filtered image saved as 'Sharpened.jpg'")
