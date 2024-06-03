import cv2
vs = cv2.VideoCapture(0)
while True:
    ret, frame = vs.read()
    if not ret:
        break
    cv2.imshow('result', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
vs.release()
cv2.destroyAllWindows()