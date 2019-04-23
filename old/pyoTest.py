# import soundUtils as su
#import pygamesoundutil as su
import pyoUtils as su
import time
    
sounds = ["Open-Hi-Hat-1.wav", "Closed-Hi-Hat-1.wav", "Hip-Hop-Snare-2.wav", "Dry-Kick.wav"]
su.loadClips(sounds)
for i in range(0,3):
   su.playClip(sounds[i])

time.sleep(1)

startTime = time.clock()

while(1):
    global startTime
    elapsed = time.clock() - startTime
    if elapsed > 0.100:
        print elapsed
        su.playClip(sounds[1])
        startTime = time.clock()
    