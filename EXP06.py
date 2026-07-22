import cv2
from tkinter import Tk, filedialog

# Hide Tkinter window
Tk().withdraw()

# Select video
video_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
)

# Open video
cap = cv2.VideoCapture(video_path)

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Normal Video", frame)

    # Normal speed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()