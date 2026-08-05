from PIL import Image, ImageFilter
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

# Check if user selected an image
if not file_path:
    print("No image selected.")
    exit()

# Open the image
im1 = Image.open(file_path)

# Apply Unsharp Mask
im2 = im1.filter(
    ImageFilter.UnsharpMask(
        radius=3,
        percent=200,
        threshold=5
    )
)

# Display the original and sharpened images
im1.show(title="Original Image")
im2.show(title="Sharpened Image")

# Save the sharpened image
im2.save("Sharpened_Image.jpg")

print("Sharpened image saved as 'Sharpened_Image.jpg'")
