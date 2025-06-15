import cv2
if __name__ == "__main__":
    cv2.namedWindow("Camera")
    vc = cv2.VideoCapture(0)
    rval = True
    if not vc.isOpened():
        rval = False
    try:
        while rval:
            rval, frame = vc.read()
            cv2.imshow("Camera", frame)
            cv2.waitKey(1)
    except KeyboardInterrupt:
        cv2.destroyWindow("Camera")
        vc.release()
