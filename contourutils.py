import cv2
import numpy as np
import imgutils as iu

def get_contours(image, minSize = 100, maxSize = 1000000000):
	return filter_contours(get_contours_raw(image), minSize, maxSize)

def get_contours_raw(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.bilateralFilter(gray, 11, 17, 17)
	edges = cv2.Canny(blur, 30, 200)
	im2, contours, hierarchy = cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
	return contours
	
def filter_contours(contours, minSize = 100, maxSize = 100000000):
	return [contour for contour in contours if cv2.contourArea(contour) > minSize and cv2.contourArea(contour) < maxSize]
	

def get_contours_unless_max(image, minSize = 100, maxSize = 100000000):
	# returns contours ONLY if there are none bigger than maxSize
	contours = get_contours(image)
	area = largest_contour_area(contours)
	if area <= maxSize:
		return [contour for contour in contours if cv2.contourArea(contour) > minSize and cv2.contourArea(contour) < maxSize]
	
def draw_contours(image, contours):
    ret = image.copy()        
    for cnt in contours:
        draw_contour(ret, cnt)
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        p = centroid(cnt)
        iu.drawText(ret, str(area), x, y, 0.25)
        iu.drawCircle(ret, p[0], p[1], 3)
    return ret
    
def draw_contour(image, contour):
    cv2.drawContours(image, [contour], -1, (0,255,0), 2)
    
def largest_contour(contours):
    if len(contours) > 0:
        cnt = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        epsilon = 0.02*cv2.arcLength(cnt,True)
        appx = cv2.approxPolyDP(cnt,epsilon,True)
        return appx
        
def largest_contour_area(contours):
	lg = largest_contour(contours)
	if lg is not None:
		return cv2.contourArea(lg)
		
def centroid(contour):
    M = cv2.moments(contour)
    cx = 0
    cy = 0
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    return [cx, cy]
    
def bounding_box(contours):
	ret = None
	lc = largest_contour(contours)
	if lc is not None:
		if len(lc) == 4:
			ret = lc
	return ret
