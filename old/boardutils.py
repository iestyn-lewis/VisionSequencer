import contourutils as cu
import imgutils as iu
import math

class Board:
	def __init__(self, name, dims, percents):
		self.cells = []
		self.name = name
		self.dims = dims
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
		cells = self.cells
		have = {}
		for piece in pieces:
			center = cu.centroid(piece)
			if pointInBoard(self, center):
				x = center[0] - xoff
				y = center[1] - yoff
				col = int(x / cw)
				row = int(y / rh)
				# determine if we are in upper or lower 
				upper = 0
				if y - (row * rh) < (rh / 4):
					upper = 1
				key = str(col) + "_" + str(row)
				if key not in have:
					have[key] = True
					cells.append([row,col,upper])
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
				upper = cell[2]
				color = (0,0,255)
				if len(cell) > 3:
					color = cell[3]
				x = int(xoff + cw * col)
				w = int(cw)
				y = int(yoff + rh * row)
				h = int(rh)
				if upper == 1:
					h = int(rh/2)
				iu.drawRectangle(image, x, y, w, h, color, 1)
		return image
		
	def highlight_beat(self, image, beat):
		cw = self.colWidth
		xoff = self.x
		x = int(xoff + beat * cw)
		w = int(cw)
		y = self.y
		h = self.h
		iu.drawRectangle(image, x, y, w, h)
		return image
		