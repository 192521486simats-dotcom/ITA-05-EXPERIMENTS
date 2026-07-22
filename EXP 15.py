import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the Tkinter root window
Tk().withdraw()

# Select the first image
print("Select the Source Image")
img1_path = askopenfilename(
    title="Select Source Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

# Select the second image
print("Select the Destination Image")
img2_path = askopenfilename(
    title="Select Destination Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

# Check if both images are selected
if img1_path == "" or img2_path == "":
    print("Image selection cancelled.")
else:
    # Load images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Define corresponding points
    pts1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200],
        [200, 200]
    ])

    pts2 = np.float32([
        [100, 100],
        [300, 100],
        [100, 300],
        [300, 300]
    ])

    # Compute Homography Matrix
    H, status = cv2.findHomography(pts1, pts2)

    # Apply Projective Transformation
    transformed = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

    # Display images
    cv2.imshow("Source Image", img1)
    cv2.imshow("Destination Image", img2)
    cv2.imshow("Projective Transformation", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the transformed image
    cv2.imwrite("Projective_Transformed_Image.jpg", transformed)

    print("Projective transformed image saved as 'Projective_Transformed_Image.jpg'")