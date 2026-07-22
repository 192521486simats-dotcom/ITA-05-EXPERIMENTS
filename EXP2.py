import cv2
from tkinter import Tk, filedialog

# Hide the main Tkinter window
Tk().withdraw()

# Open file dialog
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

# Read the selected image
image = cv2.imread(file_path)

if image is None:
    print("No image selected or image not found!")
else:
    gray = cv2.GaussianBlur(image, (5, 5), 10)

    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()