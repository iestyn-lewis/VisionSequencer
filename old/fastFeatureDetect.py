import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create(50)
    
    # find and draw the keypoints
    kp = fast.detect(gray,None)
    img2 = img.copy()
    cv2.drawKeypoints(img, kp, img2, color=(255,0,0))
    cv2.imshow('keypoints',img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()