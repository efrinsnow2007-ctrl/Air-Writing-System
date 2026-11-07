import cv2

print("Starting camera...")

for camera_index in range(3):
    print("Trying camera index:", camera_index)

    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    if cap.isOpened():
        print("SUCCESS! Camera index is:", camera_index)

        ret, frame = cap.read()

        if ret:
            print("Camera is working!")
            cv2.imshow("Camera Test", frame)
            cv2.waitKey(5000)

        cap.release()
        cv2.destroyAllWindows()
        break
    else:
        print("Failed")
else:
    print("No camera could be opened.")