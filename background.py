import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()

    if ret:
        cv2.imshow("My image", frame)

        if cv2.waitKey(5) == ord("q"):
            cv2.imwrite('image.jpg', frame)
            break

cap.release()
cv2.destroyAllWindows()