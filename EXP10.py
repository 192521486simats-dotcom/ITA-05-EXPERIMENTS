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

# Read image
image = cv2.imread(file_path)

if image is None:
    print("No image selected or image not found!")
else:
    # Get image height and width
    rows, cols = image.shape[:2]

    # Translation matrix (Move 100 pixels right and 50 pixels down)
    M = np.float32([[1, 0, 100],
                    [0, 1, 50]])

    # Apply translation
    moved = cv2.warpAffine(image, M, (cols, rows))

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Moved Image", moved)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()