from Instrument import Instrument
from Beat import Beat

class DrumMachine(Instrument):
	presetSounds = {'808': {'level': 1.0, 'sounds': ["808_BD2", "808_SD2", "808_HT", "808_MT", "808_LT", "808_CB", "808_CL", "808_RIM", "808_RIDE", "808_CP", "808_OH", "808_CH", "808_SNARE", "808_BASS"]},
					'909': {'level': 1.0, 'sounds': ["909_BD2", "909_CH2", "909_OH2", "909_SD2", "909_HT", "909_MT", "909_LT", "909_RIM", "909_RIDE", "909_CP", "909_OH", "909_CH", "909_SNARE", "909_BASS"]},
					'ROK': {'level': 1.0, 'sounds': ["ROK_CRASH", "ROK_RIDE2", "ROK_BASS2", "ROK_SHOT", "ROK_SS", "ROK_HT", "ROK_LT", "ROK_RIM", "ROK_RIDE", "ROK_CSH", "ROK_OH", "ROK_CH", "ROK_SNARE", "ROK_BASS"]},
					'WLD': {'level': 1.0, 'sounds': ["WLD_KRK", "WLD_TUNE", "WLD_HAMM", "WLD_TYM1", "WLD_TYM2", "WLD_BLOCK", "WLD_BNGO", "WLD_CBSA", "WLD_DJEM", "WLD_GAM", "WLD_MCA", "WLD_PERC", "WLD_SNAP", "WLD_TAMB"]}}

	def __init__(self, name, preset='808'):
		Instrument.__init__(self, name)
		self.sounds = DrumMachine.presetSounds[preset]['sounds']
		self.level = DrumMachine.presetSounds[preset]['level']
		self.preset = preset
		self.type = 'DM'
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
			elif row >= 1:
				beat.sounds[row-1] = True
		return beats
