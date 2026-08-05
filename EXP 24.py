import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Function for High Boost Filtering
def high_boost_filter(image, boost_factor):
    kernel_size = 3

    # Averaging kernel
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)

    # Blur the image
    blur_image = cv2.filter2D(image, -1, kernel)

    # High Boost Filtering
    sharpened = cv2.addWeighted(image, 1 + boost_factor, blur_image, -boost_factor, 0)

    return sharpened

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

# Check if the user selected a file
if not file_path:
    print("No image selected.")
    exit()

# Read the image
image = cv2.imread(file_path)

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Apply High Boost Filter
sharpened_image = high_boost_filter(image, 1.5)

# Save the output image
cv2.imwrite("sharpened_image.jpg", sharpened_image)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("High Boost Filtered Image", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("High Boost filtered image saved as 'sharpened_image.jpg'")
