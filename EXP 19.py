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

# Check if the user selected a file
if not file_path:
    print("No image selected.")
    exit()

# Read image in grayscale
img = cv2.imread(file_path, 0)

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image.")
    exit()

# Apply Sobel in X direction
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel in Y direction
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to 8-bit absolute values
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# Combine X and Y edges
edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Save the output image
cv2.imwrite("Edge_detection.jpg", edges)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imshow("Combined Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Edge-detected image saved as 'Edge_detection.jpg'")
