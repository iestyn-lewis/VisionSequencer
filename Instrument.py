from ClipPlayer import ClipPlayer
from Beat import Beat
from Measure import Measure
from copy import deepcopy

class Instrument:
	def __init__(self, name):
		self.measures = [Measure()]
		self.name = name
		self.level = 1.0
		self.locked = False
		self.muted = False
		
	def setCells(self, cells, measure):
		if not self.locked:
			measure = self.measures[measure]
			data = self.cellsToData(cells)
			measure.new = data
			if measure.saved is None:
				measure.merged = data
			else:
				measure.merged = self.mergeData(measure.merged, measure.new)
		
	def getDisplayCells(self, mindex):		
		measure = self.measures[mindex]
		cells = self.dataToCells(measure.merged)
		if self.hasSavedData(mindex):
			#show saved cells in green
			for cell in cells:
				cell.append((0,255,0))
		return cells
			
	def loadClips(self, sounds):
		ClipPlayer.loadClips(sounds)
		
	def toggleMute(self):
		self.muted = not self.muted
	
	def play(self, measure, beat):
		if not self.muted:
			data = self.measures[measure].merged
			if data is not None:
				if beat in data:
					beat = data[beat]
					accent = beat.accent
					sustain = beat.sustain
					octave = beat.octave
					for pitch in beat.pitches:
						playPitch = pitch + octave * 12
						ClipPlayer.playClip(self.sounds[0], playPitch, accent, sustain)
					for sound in beat.sounds:
						ClipPlayer.playClip(self.sounds[sound], accent = accent, level=self.level)

	def save(self):
		for measure in self.measures:
			measure.saved = deepcopy(measure.merged)
			measure.new = None
		self.locked = True
		
	def edit(self):
		self.locked = False
			
	def clear(self, mindex):
		measure = self.measures[mindex]
		measure.saved = None
		measure.merged = None
		measure.new = None
			
	def hasSavedData(self, measure):
		return not self.measures[measure].saved is None
			
	def cellsToData(self, cells):
		beats = {}
		for cell in cells:
			row = cell[0]
			col = cell[1]
			if not col in beats:
				beats[col] = Beat()
			beat = beats[col]
			if row == 0:
				beat.accent = True
			elif row >= 1:
				beat.sounds[row-1] = True
		return beats

	def dataToCells(self, data):
		cells = []
		if data is not None:
			for col in data:
				beat = data[col]
				if beat.accent:
					cells.append([0,col])
				if beat.sustain:
					cells.append([1, col])
				if beat.octave == 1:
					cells.append([2, col])
				for sound in beat.sounds:
					cells.append([sound+1, col])
				for pitch in beat.pitches:
					row = 14 - pitch
					cells.append([row, col])
		return cells
			
	def mergeData(self, saved, new):
		#  add new data and "invert" old data that matches with old
		merged = deepcopy(saved)
		# color all saved cells green
		for col in new:
			newbeat = new[col]
			if col not in merged:
				merged[col] = deepcopy(newbeat)
			else:
				oldbeat = merged[col]
				oldbeat.accent = not newbeat.accent if oldbeat.accent else newbeat.accent
				oldbeat.sustain = not newbeat.sustain if oldbeat.sustain else newbeat.sustain
				for pitch in newbeat.pitches:
					if pitch in oldbeat.pitches:
						del oldbeat.pitches[pitch]
					else:
						oldbeat.pitches[pitch] = True
				for sound in newbeat.sounds:
					if sound in oldbeat.sounds:
						del oldbeat.sounds[sound]
					else:	
						oldbeat.sounds[sound] = True
		return merged