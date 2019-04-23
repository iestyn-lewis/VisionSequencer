import contourutils as cu
import imgutils as iu
import math

class Board:
	def __init__(self, name, dims, percents):
		self.cells = []
		self.name = name
		self.rows = dims[0]
		self.cols = dims[1]
		self.percents = percents
	
	def set_board_bounds(self, imwidth, imheight):
		p = self.percents
		self.x = int(imwidth * p[0])
		self.y = int(imheight * p[1])
		self.w = imwidth * p[2]
		self.h = imheight * p[3]
		self.rowHeight = self.h / self.rows
		self.colWidth = self.w / self.cols
	
	def set_cells_from_pieces(self, pieces):
		xoff = self.x
		yoff = self.y
		cw = self.colWidth
		rh = self.rowHeight
		cells = []
		have = {}
		for piece in pieces:
			center = cu.centroid(piece)
			if self.pointInBoard(center):
				x = center[0] - xoff
				y = center[1] - yoff
				col = int(x / cw)
				row = int(y / rh)
				key = str(col) + "_" + str(row)
				if key not in have:
					have[key] = True
					cells.append([row,col])
		return cells

	def pointInBoard(self, center):
		x = center[0]
		y = center[1]
		ret = False
		if self.x <= x <= self.x + self.w:
			if self.y <= y <= self.y + self.h:
				ret = True
		return ret
	
	def draw_cells(self, image, cells):
		if cells is not None:
			cw = self.colWidth
			rh = self.rowHeight
			xoff = self.x
			yoff = self.y
			for cell in cells:
				row = cell[0]
				col = cell[1]
				color = (0,0,255)
				if len(cell) > 2:
					color = cell[2]
				x = int(xoff + cw * col)
				w = int(cw)
				y = int(yoff + rh * row)
				h = int(rh)
				iu.drawRectangle(image, x, y, w, h, color, 1)
		return image
		
	def highlight_beat(self, image, beat):
		cw = self.colWidth
		xoff = self.x
		x = int(xoff + beat * cw)
		w = int(cw)
		y = int(self.y)
		h = int(self.h)
		iu.drawRectangle(image, x, y, w, h)
		return image
		