import cv2
from tkinter import Tk, filedialog

# Hide Tkinter root window
Tk().withdraw()

# Open file dialog
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

# Read the image
img = cv2.imread(file_path)

# Check if image is loaded
if img is None:
    print("Error: Image not found or not selected!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Outline using Canny", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()