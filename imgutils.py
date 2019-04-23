import cv2
import numpy as np

def drawText(image, text, x, y, fontSize=0.5, color=(255,255,255)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    return cv2.putText(image,text,(x,y), font, fontSize ,color,1,cv2.LINE_AA)
    
def drawCircle(image, x,y,circleSize):
    return cv2.circle(image, (x,y), circleSize, (0,0,255), 1 )
    
def drawRectangle(image, x, y, w, h, color=(0,0,255), size=1):
    return cv2.rectangle(image, (x,y), (x+w, y+h), color, size)  
    
def cropEdges(image, cropAmt):
	h = image.shape[0]
	w = image.shape[1]
	return image[cropAmt:h-cropAmt , cropAmt:w-cropAmt]
	
def translate(image, x, y):
	# Define the translation matrix and perform the translation
	M = np.float32([[1, 0, x], [0, 1, y]])
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

	# Return the translated image
	return shifted

def rotate(image, angle, center = None, scale = 1.0):
	# Grab the dimensions of the image
	(h, w) = image.shape[:2]

	# If the center is None, initialize it as the center of
	# the image
	if center is None:
		center = (w / 2, h / 2)

	# Perform the rotation
	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w, h))

	# Return the rotated image
	return rotated

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	# initialize the dimensions of the image to be resized and
	# grab the image size
	dim = None
	(h, w) = image.shape[:2]

	# if both the width and height are None, then return the
	# original image
	if width is None and height is None:
		return image

	# check to see if the width is None
	if width is None:
		# calculate the ratio of the height and construct the
		# dimensions
		r = height / float(h)
		dim = (int(w * r), height)

	# otherwise, the height is None
	else:
		# calculate the ratio of the width and construct the
		# dimensions
		r = width / float(w)
		dim = (width, int(h * r))

	# resize the image
	resized = cv2.resize(image, dim, interpolation = inter)

	# return the resized image
	return resized
	
def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image
	
def overlay_images(background, foreground, x_offset, y_offset):
	background[y_offset:y_offset+foreground.shape[0], x_offset:x_offset+foreground.shape[1]] = foreground
	return background