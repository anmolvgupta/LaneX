import cv2
import numpy as np
import time

while True:
    # Create black background
    frame = np.zeros((300, 200, 3), dtype=np.uint8)

    # Simulate signal switching
    t = int(time.time()) % 6

    if t < 2:
        # RED ON
        cv2.circle(frame, (100, 50), 20, (0, 0, 255), -1)
    elif t < 4:
        # YELLOW ON
        cv2.circle(frame, (100, 150), 20, (0, 255, 255), -1)
    else:
        # GREEN ON
        cv2.circle(frame, (100, 250), 20, (0, 255, 0), -1)

    # Show window
    cv2.imshow("Traffic Signal", frame)

    # Exit when pressing Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()