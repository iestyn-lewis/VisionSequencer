from Instrument import Instrument
from Beat import Beat

class Synthesizer(Instrument):
	presetSounds = { 'piano': ["piano_tpose"] ,
					 'bass': ["bass2_tpose"],
					 'organ': ["organ_tpose"],
					 'sawlead': ["sawlead_tpose"],
					 'brasslead': ["brasslead_tpose"],
					 'pad': ["pad_tpose"]}
						
	def __init__(self, name, preset='piano'):
		Instrument.__init__(self, name)
		self.sounds = Synthesizer.presetSounds[preset]
		self.preset = preset
		self.type = 'Synth'
		self.loadClips(self.sounds)
				
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
			elif row == 1:
				beat.sustain = True
			elif row == 2:
				beat.octave = 1
			#elif row == 3:
			#	beat.octave = -1
			else:
				beat.pitches[14 - row] = True
		return beats

		
