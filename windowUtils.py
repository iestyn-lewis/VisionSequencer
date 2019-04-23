import cv2

winuAppName = ['WebCamJam']
	
def showImage(image):
	if image is not None:
		cv2.imshow(winuAppName[0], image)
	
def destroy():
	cv2.destroyAllWindows()