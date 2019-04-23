import pygame

class ClipPlayer:
	clips = {}
	def __init__(self):
		pass

	def loadClips(clipNames):
		pygame.mixer.pre_init(44100, -16, 16, 512) # setup mixer to avoid sound lag
		pygame.mixer.init()
		pygame.mixer.set_num_channels(32)
		prefix = 'samples'
		for clipName in clipNames:
			if "tpose" in clipName:
				for i in range(0, 36):
					clips[clipName + "_" + str(i)] = pygame.mixer.Sound(prefix + '/' + clipName + "/" + clipName + "_" + str(i) + ".wav") 
			else:
				clips[clipName] = pygame.mixer.Sound(prefix + '/' + clipName + ".wav") 

	def playClip(clipName, shift=0, accent=False, sustain=False, level=1.0):
		volume = 0.75 * level
		if accent:
			volume = 1.0 * level
		if "tpose" in clipName:
			name = clipName + "_" + str(shift + 12)
			#clips[name].fadeout(25)
			clips[name].set_volume(volume)
			clips[name].play()
			if not sustain:
				clips[name].fadeout(500)
		else:
			clips[clipName].set_volume(volume)
			clips[clipName].play()
	