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

# Check if an image was selected
if file_path == "":
    print("No image selected.")
else:
    # Read the image
    img = cv2.imread(file_path)

    # Get image dimensions
    rows, cols = img.shape[:2]

    # Define source points
    src_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Define destination points
    dst_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [int(0.33 * cols), rows - 1],
        [int(0.66 * cols), rows - 1]
    ])

    # Compute perspective transformation matrix
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply perspective transformation
    perspective_img = cv2.warpPerspective(img, M, (cols, rows))

    # Save the output image
    cv2.imwrite("Perspective_Transformed_Image.jpg", perspective_img)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", perspective_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Perspective transformed image saved as 'Perspective_Transformed_Image.jpg'")