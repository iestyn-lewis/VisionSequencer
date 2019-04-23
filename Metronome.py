from Timer import Timer

class Metronome:
	def __init__(self, tempo = 110.0, swing = 0, beatsPerMeasure = 16):
		self.beatsPerMeasure = beatsPerMeasure
		self.currBeat = 0
		self.playing = True
		self.tempo = tempo
		self.swing = swing
		tick = 0.25 / (tempo / 60.0)
		self.timer = Timer('metronome', tick, swing)

	def beat(self):
		return self.currBeat
						
	def tick(self):
		ret = None
		if self.playing:
			if self.timer.expired():
				ret = self.currBeat
				self.currBeat  = self.currBeat + 1
				if self.currBeat == self.beatsPerMeasure:
					self.currBeat = 0
		return ret