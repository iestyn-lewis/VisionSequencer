import pygamesoundutil as su
import time

    
#sounds = ["808_BASS", "bass_tpose", "808_SNARE", "808_OH"]
sounds = ["ROK_OH"]
su.loadClips(sounds)
#for i in range(0,3):
#   su.playClip(sounds[i])

#time.sleep(1)

startTime = time.clock()
shift = 0
while(1):
	global shift
	global startTime
	elapsed = time.clock() - startTime
	if elapsed > 0.200:
		print elapsed
		su.playClip(sounds[0], shift)
		shift += 1
		if shift == 12:
			shift = 0
		startTime = time.clock()
    