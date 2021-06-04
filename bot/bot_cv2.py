import cv2
import numpy
print(dir(cv2))
print(cv2.__version__)
print(numpy.__version__)
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame', gray)
if cv2.waitKey(1) & 0xFF == ord('q'):
 cap.release()
 cv2.destroyAllWindows()