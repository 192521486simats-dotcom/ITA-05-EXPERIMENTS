import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the Tkinter root window
Tk().withdraw()

# Open file picker
file_path = askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

# Check if a file was selected
if file_path == "":
    print("No image selected.")
else:
    # Read the image
    img = cv2.imread(file_path)

    # Get translation values from the user
    tx = int(input("Enter translation in X direction: "))
    ty = int(input("Enter translation in Y direction: "))

    # Get image dimensions
    rows, cols = img.shape[:2]

    # Translation matrix
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])

    # Apply translation
    translated_img = cv2.warpAffine(img, M, (cols, rows))

    # Save the output image
    cv2.imwrite("Translated_Image.jpg", translated_img)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Translated Image", translated_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image saved successfully as 'Translated_Image.jpg'")