import cv2
import numpy as np

# List to store selected points
points = []

# Mouse callback function
def select_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append([x, y])
        print("Point Selected:", (x, y))

# Open webcam
cap = cv2.VideoCapture(0)

cv2.namedWindow("Original Frame")
cv2.setMouseCallback("Original Frame", select_points)

print("Click 4 points on the video frame.")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw selected points
    for p in points:
        cv2.circle(frame, tuple(p), 5, (0, 0, 255), -1)

    cv2.imshow("Original Frame", frame)

    # Perform perspective transform after selecting 4 points
    if len(points) == 4:
        src = np.float32(points)

        dst = np.float32([
            [0, 0],
            [400, 0],
            [400, 600],
            [0, 600]
        ])

        M = cv2.getPerspectiveTransform(src, dst)
        warped = cv2.warpPerspective(frame, M, (400, 600))

        cv2.imshow("Perspective View", warped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()