import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the Tkinter window
Tk().withdraw()

# Select an image
file_path = askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

if file_path == "":
    print("No image selected.")
else:
    # Read the image
    img = cv2.imread(file_path)

    # Get image dimensions
    rows, cols = img.shape[:2]

    # Source points
    src_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Destination points
    dst_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, int(0.7 * rows)],
        [cols - 1, int(0.7 * rows)]
    ])

    # Compute homography matrix
    M, status = cv2.findHomography(src_points, dst_points)

    # Apply homography transformation
    homography_img = cv2.warpPerspective(img, M, (cols, rows))

    # Save the output image
    cv2.imwrite("Homography_Image.jpg", homography_img)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Homography Image", homography_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image saved successfully as 'Homography_Image.jpg'")