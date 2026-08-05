import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
&#39;haarcascade_frontalface_default.xml&#39;)
cap = cv2.VideoCapture(0)
while True:
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:

cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow(&#39;Face Recognition&#39;, frame)
if cv2.waitKey(1) &amp; 0xFF == ord(&#39;q&#39;):
break
cap.release()
cv2.destroyAllWindows()
