import numpy as np
import cv2
import imgutils as iu

cap = cv2.VideoCapture(0)

appTitle = 'Visual Sequencer'
pipelineDisplayStage = 0

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()
    
    # get key input
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('1'):
        pipelineDisplayStage = 0
    elif key == ord('2'):
        pipelineDisplayStage = 1
    elif key == ord('3'):
        pipelineDisplayStage = 2
    elif key == ord('4'):
        pipelineDisplayStage = 3
    elif key == ord('5'):
        pipelineDisplayStage = 4
    elif key == ord('6'):
        pipelineDisplayStage = 5
    elif key == ord('7'):
        pipelineDisplayStage = 6
    elif key == ord('8'):
        pipelineDisplayStage = 7
    elif key == ord('9'):
        pipelineDisplayStage = 8

    if image is not None:
        # Image pipeline #
        gray = iu.gray(image)
        blurred = iu.blur(gray)     
        edges = iu.edges(blurred)
        contours = iu.contours(edges, image)
        #lines = iu.lines(edges, image)
        #corners = iu.corners(gray, image)
        #vertLines = iu.verticalLines(iu.close(image))
                
        # set up display
        pipeline = [image, gray, blurred, edges,  contours]
        captions = ['Original', 'Greyscale', 'Gaussian Blur', 'Edged', 'Contours']
        
        # add caption and display images
        pipelineDisplayStage = np.min([pipelineDisplayStage, len(pipeline) - 1])
        display = pipeline[pipelineDisplayStage]
        caption = captions[pipelineDisplayStage]
        iu.drawText(display, caption)
        cv2.imshow(appTitle, display)
        
    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()