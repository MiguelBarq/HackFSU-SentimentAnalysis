import time
import cv2

"""
Creates n jpgs over a second from webcam feed
"""
def capFrame(n):
    cap = cv2.VideoCapture(0)
    initial_time = time.time()
    i = 0

    while True:
        # Resetting i to force a max of 10 files
        if i == n:
            return

        # Capture frame-by-frame
        succ, frame = cap.read()
        curr_time = time.time()

        if (float(curr_time - initial_time) > 1/n):

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Write the frame
            cv2.imwrite("frame%d.jpg" % i, gray)
            initial_time = time.time()
            i += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
