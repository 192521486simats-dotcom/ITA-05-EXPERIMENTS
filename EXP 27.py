import cv2
import tkinter as tk
from tkinter import filedialog

# Hide Tkinter window
root = tk.Tk()
root.withdraw()

# Select image
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

if not file_path:
    print("No image selected.")
    exit()

# Read image
img = cv2.imread(file_path)

if img is None:
    print("Error: Could not load image.")
    exit()

# Crop the image
crop_img = img[10:300, 10:300]

# Save cropped image
cv2.imwrite("cropped.jpg", crop_img)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Cropped image saved as 'cropped.jpg'")

#next copy and paste
import cv2
import tkinter as tk
from tkinter import filedialog

# Hide Tkinter window
root = tk.Tk()
root.withdraw()

# Select background image
img1_path = filedialog.askopenfilename(
    title="Select Background Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

if not img1_path:
    print("No background image selected.")
    exit()

# Select foreground image
img2_path = filedialog.askopenfilename(
    title="Select Foreground Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

if not img2_path:
    print("No foreground image selected.")
    exit()

# Read images
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

if img1 is None or img2 is None:
    print("Error: Could not load one or both images.")
    exit()

# Resize foreground image if it is too large
rows, cols = img2.shape[:2]

if rows > img1.shape[0] - 50 or cols > img1.shape[1] - 50:
    scale = min(
        (img1.shape[1] - 100) / cols,
        (img1.shape[0] - 100) / rows
    )
    img2 = cv2.resize(img2, (int(cols * scale), int(rows * scale)))
    rows, cols = img2.shape[:2]

# Region of Interest
roi = img1[50:50+rows, 50:50+cols]

# Create mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Black-out the area in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only foreground from second image
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Add images
dst = cv2.add(img1_bg, img2_fg)

# Place result back
img1[50:50+rows, 50:50+cols] = dst

# Save result
cv2.imwrite("copy_paste_result.jpg", img1)

# Display result
cv2.imshow("Copy and Paste Result", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Result saved as 'copy_paste_result.jpg'")
