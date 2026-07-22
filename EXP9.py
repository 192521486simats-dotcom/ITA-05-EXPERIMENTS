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
    # Rotate image 90° clockwise
    clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Rotate image 90° counter-clockwise
    counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Clockwise Rotation", clockwise)
    cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()