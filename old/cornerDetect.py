import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # find corners
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    
    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[0,0,255]

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()