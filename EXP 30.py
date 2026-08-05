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

# Read the image
img = cv2.imread(file_path)

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image.")
    exit()

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_img = cv2.dilate(img, kernel, iterations=1)

# Save the output image
cv2.imwrite("dilated_image.jpg", dilated_img)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Dilated image saved as 'dilated_image.jpg'")
