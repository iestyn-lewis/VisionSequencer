import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners = cv2.goodFeaturesToTrack(gray,300,0.01,10)
    corners = np.int0(corners)
    
    for i in corners:
        x,y = i.ravel()
        cv2.circle(frame,(x,y),3,255,-1)
    
    plt.imshow(frame),plt.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()