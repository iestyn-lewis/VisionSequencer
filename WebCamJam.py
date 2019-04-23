import webcamUtils as wcu
import windowUtils as winu
import imgutils as iu
import warpUtils as wu
import contourutils as cu
from Timer import Timer
from Board import Board
from Sequencer import Sequencer
from Background import Background
from KeyInput import KeyInput
import cv2

sq = Sequencer()
bg = Background()
ki = KeyInput()
wcu.createCapture()
b = {'name': 'grid', 'dims': [15, 16], 'pcts': [0.03, 0.04, 0.94, 0.93]}
gridBoard = Board(b['name'], b['dims'], b['pcts'])
tu = Timer('imgproc', 0.25)

last_bounding_box = None

def play():
	sq.play()
		
while(True):
	# capture and process image
	if tu.expired():
		image = wcu.grabImage()
		play()
		image = iu.resize(image, height=300)
		image = iu.rotate(image, 180)
		if last_bounding_box is None:
			contours = cu.get_contours(image, minSize=5000)
			bounding_box = cu.bounding_box(contours)
		play()
		if bounding_box is None:
			bounding_box = last_bounding_box
		if bounding_box is not None:
			image = wu.crop_and_warp(image, bounding_box)
			if last_bounding_box is None:
				gridBoard.set_board_bounds(image.shape[1], image.shape[0])
			last_bounding_box = bounding_box
			play()
			pieces = cu.get_contours(image,  minSize=60, maxSize=300)
 			play()
			cells = gridBoard.set_cells_from_pieces(pieces)
			sq.updateCells(cells)
			gridBoard.draw_cells(image, sq.getDisplayCells())
			image = gridBoard.highlight_beat(image, sq.beat())
			play()
			image = bg.createFinalImage(image, sq)
			play()
			winu.showImage(image)
		else:
			# can't find bounding box, show raw image with contours we did find
			image = cu.draw_contours(image, cu.get_contours(image))
			image = iu.drawText(image, 'Acquiring board...', 40, 80, color=(255,0,0), fontSize=1.0)
			winu.showImage(image)
    
	play()
	
	if ki.processKeys(sq):
		break
	
wcu.destroy()
winu.destroy()
