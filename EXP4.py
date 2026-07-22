import cv2
import numpy as np
from tkinter import Tk, filedialog

# Hide Tkinter window
Tk().withdraw()

# Select image from laptop
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

# Read the image
image = cv2.imread(file_path)

if image is None:
    print("No image selected or image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5,5), np.uint8)

    # Dilate the image
    dilated = cv2.dilate(image, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()