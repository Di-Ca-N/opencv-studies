import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.haarcascades + "haarcascade_frontalface_alt.xml"
)
face_mask = cv2.imread('./images/mask_v_b.png')

if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier')


cap = cv2.VideoCapture(0)
scaling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=1)

    for (x, y, w, h) in face_rects:
        h = int(1.5 * h)
        w = int(1.5 * w)

        x -= int(w * 0.15)
        y -= int(h * 0.1)

        frame_roi = frame[y:y + h, x:x + w]
        face_mask_small = cv2.resize(
            face_mask, (w, h), interpolation=cv2.INTER_AREA)

        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)

        ret, mask = cv2.threshold(gray_mask, 252, 255, cv2.THRESH_BINARY_INV)

        mask_inv = cv2.bitwise_not(mask)

        try:
            masked_face = cv2.bitwise_and(
                face_mask_small, face_mask_small, mask=mask)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            frame[y:y + h, x:x + w] = cv2.add(masked_face, masked_frame)
        except cv2.error as e:
            print('Ignoring arithmetic exceptions: ' + str(e))

    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
