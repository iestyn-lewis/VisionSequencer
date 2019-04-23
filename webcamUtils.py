import cv2

wcuCap = [None]

def createCapture():
	wcuCap[0]= cv2.VideoCapture(1)

def grabImage():
	ret, image = wcuCap[0].read()
	return image
	
def destroy():
	wcuCap[0].release()