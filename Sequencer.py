from Metronome import Metronome
from DrumMachine import DrumMachine
from Synthesizer import Synthesizer

class Sequencer:
	defInsts = [{'name': '808', 'type': 'dm', 'preset': '808'},
				   {'name': '909', 'type': 'dm', 'preset': '909'},
				   {'name': 'Rock', 'type': 'dm', 'preset': 'ROK'},
				   {'name': 'World', 'type': 'dm', 'preset': 'WLD'},
				   {'name': 'Bass', 'type': 'sy', 'preset': 'bass'},
				   {'name': 'Piano', 'type': 'sy', 'preset': 'piano'},
				   {'name': 'Organ', 'type': 'sy', 'preset': 'organ'},
				   {'name': 'Saw', 'type': 'sy', 'preset': 'sawlead'},
				   {'name': 'Square', 'type': 'sy', 'preset': 'brasslead'},
				   {'name': 'Pad', 'type': 'sy', 'preset': 'pad'}
				]
				
	def __init__(self):
		self.metronome = Metronome(60, 0.0)
		self.instruments = []
		self.measuresPerPattern = 1
		self.firstMeasure = True
		self.currMeasure = 0
		self.editMeasure = 0
		self.loopMeasure = False
		self.fillMeasure = False
		self.mode = 'rec'
		self.currInst = None
		for inst in Sequencer.defInsts:
			if inst['type'] == 'dm':
				self.instruments.append(DrumMachine(inst['name'], inst['preset']))
			if inst['type'] == 'sy':
				self.instruments.append(Synthesizer(inst['name'], inst['preset']))
				
		# assign first
		self.currInst = self.instruments[0]
		
	def beat(self):
		return self.metronome.beat()
		
	def setCurrInst(self, index):
		if self.currInst is not None:
			if not self.currInst.locked:
				self.currInst.clear(self.editMeasure)
		self.currInst = self.instruments[index]
		
	def toggleMute(self, index):
		self.instruments[index].toggleMute()
		
	def saveCurrInst(self):
		self.currInst.save()
						
	def play(self):
		beat = self.metronome.tick()
		if beat is not None:
			if beat == 0:
				if not self.firstMeasure and not self.loopMeasure:
					self.currMeasure = self.currMeasure + 1
					if self.currMeasure >= self.measuresPerPattern:
						self.currMeasure = 0
				else:
					self.firstMeasure = False
			for inst in self.instruments:
				inst.play(self.currMeasure, beat)
			
	def updateCells(self, cells):
		if self.editMeasure is not None:
			if self.editMeasure == self.currMeasure:
				if self.mode == 'rec':
					if self.currInst is not None:
						self.currInst.setCells(cells, self.editMeasure)

	def getDisplayCells(self):
		if self.currInst is not None:
			return self.currInst.getDisplayCells(self.currMeasure)
