import cv2
from tkinter import Tk, filedialog

# Hide root window
Tk().withdraw()

# Open file dialog to select image
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
    cv2.imshow("Original Image", img)

    # Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)

    
    # Save grayscale image
    cv2.imwrite("gray_image.jpg", gray)

    print("Image processed successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()