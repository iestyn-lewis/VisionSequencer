import imgutils as iu

class Background:
	captions = {'DM': ['>', 'PRC 1', 'PRC 2', 'PRC 3', 'H TOM', 'M TOM', 'L TOM', 'CRASH', 'BELL', 'RIM', 'RIDE', 'O HAT', 'C HAT', 'SNARE', 'KICK'],
				'Synth': ['>', 'SUS', 'OCT', 'B', 'Bb', 'A', 'Ab', 'G', 'F#', 'F', 'E', 'Eb', 'D', 'C#', 'C']}

	def __init__(self):
		self.backgroundImage = None
		
	def createBackgroundImage(self, image, sq):
		image = iu.create_blank(image.shape[1] + 100, 700)
		text = 'Select instrument with number keys.  Shift + number to mute/unmute.'
		image = iu.drawText(image, text, 20, 70)
		text = 'WebCamJam   ---   Q to Quit'
		image = iu.drawText(image, text, 200, 680)	
		x = 10
		y = 185
		for lc in Background.captions[sq.currInst.type]:
			iu.drawText(image, lc, x, y, fontSize=0.35)
			y += 31
		x = 87
		y = 140
		for i in range(0,16):
			iu.drawText(image, str(i + 1), x, y, fontSize = 0.35)
			x += 34
		return image
		
	def createFinalImage(self, image, sq):
		image = iu.resize(image, height=500)
		self.backgroundImage = self.createBackgroundImage(image, sq)
		image = iu.overlay_images(self.backgroundImage, image, 60, 150)
		image = self.drawStatusText(image, sq)
		return image
		
	def drawStatusText(self, image, sq):
		x = 20
		y = 40
		i = 1
		for inst in sq.instruments:
			if i == 10:
				i = 0
			color = (255,255,255)
			if inst == sq.currInst:
				color = (0,0,255)
			if inst.hasSavedData(sq.currMeasure):
				color = (0, 255, 0)
			if inst == sq.currInst:
				image = iu.drawRectangle(image, x-5, y-35, 65, 40, color=color, size=1)
			image = iu.drawText(image, inst.name, x, y, color=color)
			image = iu.drawText(image, str(i), x, y-15, color=color)
			if inst.muted:
				image = iu.drawText(image, 'MUTE', x + 17, y-15, color=(0,0,255))
			x += 65
			i += 1
		if sq.currInst.hasSavedData(sq.currMeasure):
			text = 'Saved Instrument Data'
			color = (0,255,0)
		else:
			text = "Unsaved Data (S to Save)"
			color = (0,0,255)
		image = iu.drawText(image, text, 20, 100, color=color)
		return image