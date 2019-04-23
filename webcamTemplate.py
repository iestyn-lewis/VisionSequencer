import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
cv2.namedWindow('Output')

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()

    if image is not None:
        # CODE #
        
        # Display the resulting frame
        cv2.imshow('Output',image)
        
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()