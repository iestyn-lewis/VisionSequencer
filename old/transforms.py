import cv2
import numpy as np

def original(image):
    return image    
    
def gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
def blur(image):
    return cv2.GaussianBlur(image, (11, 11), 0) 
    
def edges(image):
    return cv2.Canny(image, 30, 150)
    
def contours(edges, image):
    im2, contours, hierarchy = cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    ret = image.copy()
    if len(contours) > 0:
        print "# of contours: %s" % (len(contours))
        print "contours[0][0]: %s" % (contours[0][0])
        cv2.drawContours(ret, contours, -1, (0,255,0), 2)
    return ret
        
def lines(edges, image):
    ret = image.copy()
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=200,maxLineGap=10)
    if lines is not None:
        for line in lines:
           x1,y1,x2,y2 = line[0]
           cv2.line(ret,(x1,y1),(x2,y2),(0,255,0),2)   
    return ret
    
def corners(gray, image):
    # find corners
    retimage = image.copy()
    gray2 = np.float32(gray)
    dst = cv2.cornerHarris(gray2,2,3,0.04)
    
    #result is dilated for marking the corners, not important
    # dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst, connectivity=4)
    
    # Threshold for an optimal value, it may vary depending on the image.
    # frame[dst>0.01*dst.max()]=[0,0,255]
    # display centroids
    for centroid in centroids:
        retimage = cv2.circle(retimage, (int(centroid[0]), int(centroid[1])), 5, (0,0,255), 1 )
    return retimage

def close(image):
    img = cv2.GaussianBlur(image,(5,5),0)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    mask = np.zeros((gray.shape),np.uint8)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))  
    close = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel1)
    div = np.float32(gray)/(close)
    res = np.uint8(cv2.normalize(div,div,0,255,cv2.NORM_MINMAX))
    return res

def verticalLines(image):
    kernelx = cv2.getStructuringElement(cv2.MORPH_RECT,(2,10))
    dx = cv2.Sobel(image,cv2.CV_16S,1,0)
    dx = cv2.convertScaleAbs(dx)
    cv2.normalize(dx,dx,0,255,cv2.NORM_MINMAX)
    ret,close = cv2.threshold(dx,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    close = cv2.morphologyEx(close,cv2.MORPH_DILATE,kernelx,iterations = 1)
    
    im2, contour, hier = cv2.findContours(close,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour:
        x,y,w,h = cv2.boundingRect(cnt)
        if h/w > 5:
            cv2.drawContours(close,[cnt],0,255,-1)
        else:
            cv2.drawContours(close,[cnt],0,0,-1)
    close = cv2.morphologyEx(close,cv2.MORPH_CLOSE,None,iterations = 2)
    return close
