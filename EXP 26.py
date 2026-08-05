import cv2
import tkinter as tk
from tkinter import filedialog

# Hide the Tkinter window
root = tk.Tk()
root.withdraw()

# Select the logo image
logo_path = filedialog.askopenfilename(
    title="Select the Logo Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

if not logo_path:
    print("No logo image selected.")
    exit()

# Select the background image
image_path = filedialog.askopenfilename(
    title="Select the Background Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

if not image_path:
    print("No background image selected.")
    exit()

# Read the images
logo = cv2.imread(logo_path)
img = cv2.imread(image_path)

# Check if images loaded successfully
if logo is None or img is None:
    print("Error: Could not load one or both images.")
    exit()

# Get dimensions
h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape

# Resize logo if it is larger than the background image
if h_logo > h_img or w_logo > w_img:
    scale = min(h_img / h_logo, w_img / w_logo) * 0.5
    new_width = int(w_logo * scale)
    new_height = int(h_logo * scale)
    logo = cv2.resize(logo, (new_width, new_height))
    h_logo, w_logo = logo.shape[:2]

# Calculate center position
center_y = h_img // 2
center_x = w_img // 2

top_y = center_y - h_logo // 2
left_x = center_x - w_logo // 2
bottom_y = top_y + h_logo
right_x = left_x + w_logo

# Overlay the logo
destination = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(destination, 1.0, logo, 0.5, 0)

# Place the result back
img[top_y:bottom_y, left_x:right_x] = result

# Save the watermarked image
cv2.imwrite("watermarked.jpg", img)

# Display the result
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Watermarked image saved as 'watermarked.jpg'")
