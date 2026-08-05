import cv2
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

# Read image in grayscale
img = cv2.imread(file_path, 0)

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image.")
    exit()

# Apply Sobel Y Edge Detection
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)

# Save the output image
cv2.imwrite("sobel_y.jpg", sobel_y)

# Display original and Sobel Y images
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Sobel Y image saved as 'sobel_y.jpg'")
