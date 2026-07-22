import cv2
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
    # Scale image to bigger size (2x)
    bigger = cv2.resize(image, None, fx=2, fy=2)

    # Scale image to smaller size (0.5x)
    smaller = cv2.resize(image, None, fx=0.5, fy=0.5)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()