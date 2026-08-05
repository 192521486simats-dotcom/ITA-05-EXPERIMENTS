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

# Define the sharpening kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

# Apply convolution
sharpened_img = cv2.filter2D(img, -1, kernel)

# Save the output image
cv2.imwrite("convolutional_image.jpg", sharpened_img)

# Display images
cv2.imshow("Input Image", img)
cv2.imshow("Convolutional Image", sharpened_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Convolutional image saved as 'convolutional_image.jpg'")
