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

# Read the image
input_image = cv2.imread(file_path)

# Check if image loaded successfully
if input_image is None:
    print("Error: Could not load image.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Create a 3x3 rectangular structuring element
filterSize = (3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)

# Apply Black Hat operation
blackhat_img = cv2.morphologyEx(gray_image, cv2.MORPH_BLACKHAT, kernel)

# Save the output image
cv2.imwrite("blackhat.jpg", blackhat_img)

# Display the images
cv2.imshow("Original Image", gray_image)
cv2.imshow("Black Hat Image", blackhat_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Black Hat image saved as 'blackhat.jpg'")
